"""Custom loader for loading lessons."""

import os.path
from django.core.exceptions import ObjectDoesNotExist
from utils.BaseLoader import BaseLoader
from utils.convert_heading_tree_to_dict import convert_heading_tree_to_dict
from utils.errors.MissingRequiredFieldError import MissingRequiredFieldError
from utils.errors.KeyNotFoundError import KeyNotFoundError
from utils.errors.InvalidConfigValueError import InvalidConfigValueError

from topics.models import (
    ProgrammingChallenge,
    ProgrammingChallengeNumber,
    LearningOutcome,
    Resource,
    ResourceDescription,
)


class LessonsLoader(BaseLoader):
    """Custom loader for loading lessons."""

    def __init__(self, lessons_structure_file_path, topic, unit_plan, BASE_PATH):
        """Create the loader for loading lessons.

        Args:
            lessons_structure_file_path: file path to lessons yaml file (str).
            topic: Object of Topic model (Topic).
            unit_plan: Object of UnitPlan model (UnitPlan).
            BASE_PATH: Base file path (str).
        """
        super().__init__(BASE_PATH)
        self.lessons_structure_file_path = lessons_structure_file_path
        self.topic = topic
        self.unit_plan = unit_plan

    def load(self):
        """Load the content for a single lesson.

        Raises:
            KeyNotFoundError: when no object can be found with the matching attribute.
            InvalidConfigValueError: when provided value is not valid.
            MissingRequiredFieldError: when a value for a required model field cannot be
                found in the config file.
        """
        lessons_structure = self.load_yaml_file(self.lessons_structure_file_path)

        for (lesson_slug, lesson_structure) in lessons_structure.items():

            if lesson_structure is None:
                raise MissingRequiredFieldError(
                    self.lessons_structure_file_path,
                    ["number"],
                    "Lesson"
                )

            # Build the file path to the lesson"s md file
            file_path = os.path.join(
                self.BASE_PATH,
                "lessons",
                "{}.md".format(lesson_slug)
            )

            lesson_content = self.convert_md_file(
                file_path,
                self.lessons_structure_file_path,
            )

            if "computational-thinking-links" in lesson_structure:
                file_name = lesson_structure["computational-thinking-links"]
                file_path = os.path.join(
                    self.BASE_PATH,
                    "lessons",
                    file_name
                )
                ct_links_content = self.convert_md_file(
                    file_path,
                    self.lessons_structure_file_path,
                    heading_required=False,
                    remove_title=False,
                )
                ct_links = ct_links_content.html_string
            else:
                ct_links = None

            if "duration" in lesson_structure:
                lesson_duration = lesson_structure["duration"]
            else:
                lesson_duration = None

            heading_tree = None
            if lesson_content.heading_tree:
                heading_tree = convert_heading_tree_to_dict(lesson_content.heading_tree)

            if "programming-challenges-description" in lesson_structure:
                file_name = lesson_structure["programming-challenges-description"]
                file_path = os.path.join(
                    self.BASE_PATH,
                    "lessons",
                    file_name
                )
                programming_description_content = self.convert_md_file(
                    file_path,
                    self.lessons_structure_file_path,
                    heading_required=False,
                    remove_title=False,
                )
                programming_description = programming_description_content.html_string
            else:
                programming_description = None

            classroom_resources = lesson_structure.get("classroom-resources", None)
            if isinstance(classroom_resources, list):
                for classroom_resource in classroom_resources:
                    if not isinstance(classroom_resource, str):
                        raise InvalidConfigValueError(
                            self.lessons_structure_file_path,
                            "classroom-resources list item",
                            "A string describing the classroom resource."
                        )
                    elif len(classroom_resource) > 100:
                        raise InvalidConfigValueError(
                            self.lessons_structure_file_path,
                            "classroom-resources list item",
                            "Item description must be less than 100 characters."
                        )
            elif classroom_resources is not None:
                raise InvalidConfigValueError(
                    self.lessons_structure_file_path,
                    "classroom-resources",
                    "List of strings."
                )

            lesson = self.topic.lessons.create(
                unit_plan=self.unit_plan,
                slug=lesson_slug,
                name=lesson_content.title,
                duration=lesson_duration,
                content=lesson_content.html_string,
                computational_thinking_links=ct_links,
                heading_tree=heading_tree,
                programming_challenges_description=programming_description,
                classroom_resources=classroom_resources,
            )
            lesson.save()

            # Add programming challenges
            if "programming-challenges" in lesson_structure:
                programming_challenge_slugs = lesson_structure["programming-challenges"]
                if programming_challenge_slugs is not None:
                    # Check all slugs are valid
                    for programming_challenge_slug in programming_challenge_slugs:
                        try:
                            ProgrammingChallenge.objects.get(
                                slug=programming_challenge_slug,
                                topic=self.topic
                            )

                        except ObjectDoesNotExist:
                            raise KeyNotFoundError(
                                self.lessons_structure_file_path,
                                programming_challenge_slug,
                                "Programming Challenges"
                            )

                    # Store number of challenge in relationship with lesson.
                    # If three linked challenges have numbers 1.1, 4.2, and 4.5
                    # They will be stored as 1.1, 2.1, and 2.2 respectively.

                    # Order challenges for numbering.
                    programming_challenges = ProgrammingChallenge.objects.filter(
                        slug__in=programming_challenge_slugs,
                        topic=self.topic
                    ).order_by("challenge_set_number", "challenge_number")

                    # Setup variables for numbering.
                    display_set_number = 0
                    last_set_number = -1
                    display_number = 0
                    last_number = -1

                    # For each challenge, increment number variables if original
                    # numbers are different.
                    for programming_challenge in programming_challenges:
                        if programming_challenge.challenge_set_number > last_set_number:
                            display_set_number += 1
                            display_number = 0
                            last_number = -1
                        if programming_challenge.challenge_number > last_number:
                            display_number += 1
                        last_set_number = programming_challenge.challenge_set_number
                        last_number = programming_challenge.challenge_number

                        # Create and save relationship between lesson and
                        # challenge that contains challenge number.
                        relationship = ProgrammingChallengeNumber(
                            programming_challenge=programming_challenge,
                            lesson=lesson,
                            challenge_set_number=display_set_number,
                            challenge_number=display_number,
                        )
                        relationship.save()

            # Add learning outcomes
            if "learning-outcomes" in lesson_structure:
                learning_outcome_slugs = lesson_structure["learning-outcomes"]
                if learning_outcome_slugs is not None:
                    for learning_outcome_slug in learning_outcome_slugs:
                        try:
                            learning_outcome = LearningOutcome.objects.get(
                                slug=learning_outcome_slug
                            )
                            lesson.learning_outcomes.add(learning_outcome)
                        except ObjectDoesNotExist:
                            raise KeyNotFoundError(
                                self.lessons_structure_file_path,
                                learning_outcome_slug,
                                "Learning Outcomes"
                            )

            # Add generated resources
            if "generated-resources" in lesson_structure:
                resources = lesson_structure["generated-resources"]
                if resources is not None:
                    for (resource_slug, resource_data) in resources.items():
                        if resource_data is None:
                            raise MissingRequiredFieldError(
                                self.lessons_structure_file_path,
                                ["description"],
                                "Generated Resource"
                            )
                        try:
                            resource = Resource.objects.get(
                                slug=resource_slug
                            )
                        except ObjectDoesNotExist:
                            raise KeyNotFoundError(
                                self.lessons_structure_file_path,
                                resource_slug,
                                "Resources"
                            )
                        resource_description = resource_data.get("description", None)
                        if resource_description is None:
                            raise MissingRequiredFieldError(
                                self.lessons_structure_file_path,
                                ["description"],
                                "Generated Resource"
                            )

                        relationship = ResourceDescription(
                            resource=resource,
                            lesson=lesson,
                            description=resource_description
                        )
                        relationship.save()

            self.log("Added lesson: {}".format(lesson.__str__()), 2)
