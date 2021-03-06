"""Custom loader for loading a topic."""

import os.path
from django.db import transaction

from utils.BaseLoader import BaseLoader
from utils.check_required_files import find_image_files

from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError

from topics.models import Topic


class TopicLoader(BaseLoader):
    """Custom loader for loading a topic."""

    def __init__(self, factory, structure_file_path, BASE_PATH):
        """Create the loader for loading a topic.

        Args:
            factory: LoaderFactory object for creating loaders (LoaderFactory).
            structure_file_path: File path for structure YAML file (str).
            BASE_PATH: Base file path (str).
        """
        super().__init__(BASE_PATH)
        self.factory = factory
        self.topic_slug = os.path.split(structure_file_path)[0]
        self.structure_file_path = os.path.join(self.BASE_PATH, structure_file_path)
        self.BASE_PATH = os.path.join(self.BASE_PATH, self.topic_slug)

    @transaction.atomic
    def load(self):
        """Load the content for a topic.

        Raise:
            MissingRequiredFieldError: when no object can be found with the matching
                attribute.
        """
        topic_structure = self.load_yaml_file(self.structure_file_path)

        unit_plans = topic_structure.get("unit-plans", None)
        if unit_plans is None:
            raise MissingRequiredFieldError(
                self.structure_file_path,
                ["unit-plans"],
                "Topic"
            )

        # Convert the content to HTML
        topic_content = self.convert_md_file(
            os.path.join(
                self.BASE_PATH,
                "{}.md".format(self.topic_slug)
            ),
            self.structure_file_path
        )

        # If other resources are given, convert to HTML
        if "other-resources" in topic_structure:
            topic_other_resources_file = topic_structure["other-resources"]
            if topic_other_resources_file is not None:
                other_resources_content = self.convert_md_file(
                    os.path.join(
                        self.BASE_PATH,
                        topic_other_resources_file
                    ),
                    self.structure_file_path
                )
                topic_other_resources_html = other_resources_content.html_string
            else:
                topic_other_resources_html = None
        else:
            topic_other_resources_html = None

        # Check if icon is given
        if "icon" in topic_structure:
            topic_icon = topic_structure["icon"]
            if topic_icon is not None:
                find_image_files([topic_icon], self.structure_file_path)
            else:
                topic_icon = None
        else:
            topic_icon = None

        # Create topic objects and save to the db
        topic = Topic(
            slug=self.topic_slug,
            name=topic_content.title,
            content=topic_content.html_string,
            other_resources=topic_other_resources_html,
            icon=topic_icon
        )
        topic.save()

        self.log("Added Topic: {}".format(topic.name))

        # Load programming challenges
        if "programming-challenges" in topic_structure:
            programming_challenges_structure_file_path = topic_structure["programming-challenges"]
            if programming_challenges_structure_file_path is not None:
                self.factory.create_programming_challenges_loader(
                    programming_challenges_structure_file_path,
                    topic,
                    self.BASE_PATH
                ).load()

        # Load unit plans
        for unit_plan_file_path in unit_plans:
            self.factory.create_unit_plan_loader(
                unit_plan_file_path,
                topic,
                self.BASE_PATH
            ).load()

        if "curriculum-integrations" in topic_structure:
            curriculum_integrations_structure_file_path = topic_structure["curriculum-integrations"]
            if curriculum_integrations_structure_file_path is not None:
                self.factory.create_curriculum_integrations_loader(
                    curriculum_integrations_structure_file_path,
                    topic,
                    self.BASE_PATH
                ).load()

        self.log("")
