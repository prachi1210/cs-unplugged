Topic Content
##############################################################################

The topics application (see :ref:`what-is-an-application`) is the main focus of
the CS Unplugged website, as it contains the majority of educational material
for the project.

.. contents:: Contents
  :local:

Topics Overview
==============================================================================

A general overview of the topics application can be described in the following
diagram.

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. image:: ../_static/img/topics_overview_diagram.png
  :alt: A diagram providing an overview of topics application content

- The application is made up of **topics**.

  - A **topic** must contain at least one **unit plan**.

    - A **unit plan** must contain at least one **lesson**.

      - A **lesson** can contain **learning outcomes**, **curriculum areas**, and **generated
        resources**.

  - A **topic** can also contain **curriculum integrations**, which can also contain
    **curriculum areas**.

  - A **topic** can also contain **programming exercises**.

    - A **programming exercise** can use different **programming languages**, and be set at
      a specific **difficulty**.

- **Learning outcomes**, **curriculum areas**, **programming languages**, and
  **difficulties** are defined at a language level, so can be used by all topic content
  of that language.

This is just a broad overview of the topics application.


.. _viewing-the-current-state:

Viewing the Current State
------------------------------------------------------------------------------

When developing locally, once you have a server and ``gulp`` running (see
:doc:`../getting_started/basic_usage`) you can go to the url below to get a
quick overview of what content is loaded:

.. code-block:: none

  localhost:3000/__dev__/

For more information about what this page displays, see :doc:`../developer/dev`.

.. _topics-directory-structure:

Topics Content Directory
==============================================================================

The diagram below is an example of the ``content/en/`` language directory for
the project's topic application, where:

- Blue is directories.
- Red is YAML configuration files (see :doc:`understanding_configuration_files`).
- Green is Markdown text files.

.. raw:: html
  :file: ../_static/html_snippets/topics_content_directory_tree.html

.. _adding-topics-content:

Adding Content
==============================================================================

The following flow charts will take you step by step through the process of adding new
content to the topics application. Below this section is full details on how to structure
and write the configuration files for the topics application.

.. _adding-topics-content-topics:

Adding a Topic
------------------------------------------------------------------------------

.. The following image can copied for be edits here:
.. image:: ../_static/img/topics_adding_topic_flowchart.png

.. warning::
  
  Every topic needs at least one unit plan, therefore the system will not allow
  a topic to be loaded until a unit plan is connected to it.

.. _adding-topics-content-unit-plans:

Adding a Unit Plan
------------------------------------------------------------------------------

.. The following image can copied for be edits here:
.. image:: ../_static/img/topics_adding_unit_plan_flowchart.png

.. warning::
  
  Every unit plan needs at least one lesson, so the system will not allow a
  unit plan to be loaded until a lesson is connected to it.


.. _adding-topics-content-lessons:

Adding a Lesson
------------------------------------------------------------------------------

.. The following image can copied for be edits here:
.. image:: ../_static/img/topics_adding_lesson_flowchart.png

.. note::
  
  If the lesson includes programming exercises, curriculum areas, and/or
  learning outcomes, then the corresponding configuration and content files
  will also need to be added.


.. _adding-topics-content-learning-outcomes:

Adding Learning Outcomes
------------------------------------------------------------------------------

.. The following image can copied for be edits here:
.. image:: ../_static/img/topics_adding_learning_outcomes_flowchart.png

You will now be able to add learning outcomes to lessons and programming
exercises by referencing the keys you specified in the learning outcomes configuration
file.


.. _adding-topics-content-curriculum-areas:

Adding Curriculum Areas
------------------------------------------------------------------------------

.. The following image can copied for be edits here:
.. image:: ../_static/img/topics_adding_curriculum_areas_flowchart.png

You will now be able to add curriculum areas to lessons and curriculum
integrations by referencing the keys you specified in the curriculum areas
configuration file.


.. _adding-topics-content-programming-exercises:

Adding a Programming Exercise
------------------------------------------------------------------------------

.. The following image can copied for be edits here:
.. image:: ../_static/img/topics_adding_programming_exercises_flowchart.png

You will now be able to add programming exercises to lessons by referencing the
keys you specified in the programming exercises configuration file.

.. note::

  If the exercise includes learning outcomes, then the corresponding configuration
  file will also need to be added or updated to include new learning outcomes.

.. note::

  A programming exercise is split into four parts, these are:

    1. The exercise description
    2. The expected output
    3. Hints (optional)
    4. Example solution(s)

  Additonally, 2-4 from the list above, can be given in multiple programming
  languages. Therefore, the languages you have chosen must be specified in the
  ``programming-exercises.yaml`` configuration file, as well as the
  ``programming-exercises-structure.yaml`` configuration file.

.. note::

  The system will use the key for the programming exercise to search for the
  relevant Markdown files, so it is important to name them according to the
  following rules:

  - Both the directory and file name for the exercise must match the key you chose
    for the exercise in ``programming-exercises.yaml``
  
  - The expected, hints, and solution files must be prefixed with the key for
    the programming language they are written in.

  For example, a programming exercise with key ``count-to-16`` implemented in
  Python only will have the following directory structure:

  .. code-block:: none

    └── programming-exercises/
        └── count-to-16/
            ├── count-to-16.md
            ├── python-expected.md
            ├── python-hints.md
            └── python-solution.md


.. _adding-topics-content-curriculum-integrations:

Adding a Curriculum Integration
------------------------------------------------------------------------------

.. The following image can copied for be edits here:
.. image:: ../_static/img/topics_adding_curriculum_integrations_flowchart.png

.. note ::

  If the integration includes curriculum areas and/or prerequisite lessons,
  then the corresponding configuration and content files will also need to be added.


Configuration Files
==============================================================================

This section details configuration files within the ``content`` directory for a specific
language.
These files are in YAML format. If you are not familiar with YAML, see
:doc:`understanding_configuration_files`.

The diagram below shows an example of YAML file locations for the
``content/en/`` language directory, where:

- Blue is directories.
- Red is YAML configuration files.

.. raw:: html
  :file: ../_static/html_snippets/topics_content_directory_tree_only_yaml.html

In the following sections, each configuration file is exaplained in more detail.

.. note::
  
  - We use the term "key" to specify a field name. Keys map to particular values (which
    range from learning outcome text, to the structure and attributes of a lesson).
    There are two things to remember with keys:

    - They must be written in lowercase and use hyphens instead of spaces.

    - They must be exact matches to work, for example, if you name a lesson
      ``bits-and-bytes``, referencing it in another configuration file as
      ``bytes-and-bits`` will raise an error.

.. note::

  - Some of the keys have angle brackets around them, ``<like so>``. This means that they
    are variables and you can call them whatever you like in your configuration file
    (without the angle brackets).


.. _application-structure-file:

Application Structure Configuration File
------------------------------------------------------------------------------

- **File Name:** ``structure.yaml``

- **Location:** ``topics/content/<language>/``

- **Purpose:** Defines the top level configuration files to process for defining
  the content of the topics application.

- **Required Fields:**

  - ``topics``: A list of file paths to topic configuration files.

- **Optional Fields:**

    - ``learning-outcomes:`` The path to the learning outcomes configuration file.
    - ``curriculum-areas:`` The path to the curriculum areas configuration file.
    - ``programming-exercises-structure:`` The path to the programming exercies structure
      configuration file.

A complete application structure file may look like the following:

.. code-block:: yaml

  topics:
    - binary-numbers
    - error-detection-correction

  learning-outcomes: learning-outcomes.yaml
  curriculum-areas: curriculum-areas.yaml
  programming-exercises-structure: programming-exercises-structure.yaml

.. _topic-file:

Topic Configuration File
------------------------------------------------------------------------------

- **File Name:** ``<topic-name>.yaml``

- **Location:** ``topic/content/<language>/<topic-name>/``

- **Referenced In:** ``topic/content/<launguage>/structure.yaml``

- **Purpose:** This file defines the attributes of a specific topic, including connected
  unit plan, programming exercise, and curriculum integration configuration files.

- **Required Fields:**

  - ``unit-plans:`` A list of keys, where each key is a unit plan.

- **Optional Fields:**

  - ``icon:`` An image file to be used as the icon for the topic.

  - ``other-resources:`` A Markdown file containing information about other related
    (external) resources.

  - ``programming-exercises:`` The path to the programming exercises configuration file.

  - ``curriculum-integrations:`` The path to the curriculum integrations configuration
    file.

A complete topic structure file may look like the following:

.. code-block:: yaml

  unit-plans:
    - unit-plan
    - unit-plan-2

  icon: img/binary-numbers-0-1.png

  other-resources: other-resources.md

  programming-exercises: programming-exercises/programming-exercises.yaml
  curriculum-integrations: curriculum-integrations/curriculum-integrations.yaml


.. _unit-plan-file:

Unit Plan Configuration File
------------------------------------------------------------------------------

- **File Name:** ``<unit-plan-name>.yaml``

- **Location:** ``topic/content/<language>/<topic-name>/<unit-plan-name>/``

- **Referenced In:** ``topic/content/<language>/<topic-name>/<topic-name>.yaml``

- **Purpose:** This file defines all the lessons (and their respective)
  attributes for the unit plan.

  - **Required Fields:**

    - ``<lesson-name>:`` This is the key for the lesson. Each lesson has its own list of
      required and optional fields:

      - **Required Fields:**

        - ``min-age:`` The suggested minimum age group to teach this lesson to.

        - ``max-age:`` The suggested maximum age group to teach this lesson to.

        - ``number:`` The number order for this lesson.
          Lessons are grouped by their minimum age and maximum age, then ordered by
          number so lessons in different age groups can use the same number without
          conflict.

      - **Optional Fields:**

        - ``duration``: The estimated time to complete the lesson (in minutes).

        - ``programming-exercises:`` A list of keys corresponding to programming
          exercises.

        - ``learning-outcomes:`` A list of keys corresponding to learning outcomes.

        - ``curriculum-areas:`` A list of keys corresponding to other curriculum areas
          that this lesson could be taught in.

        - ``generated-resources:`` A list of generated CSU resources connected to this
          lesson.

          - **Required Fields:**:

            - ``<resource>``: The key corresponding to the resource.

              - **Required Fields:**:

                - ``description:`` A description of how the resource should be used.

A complete unit plan structure file with multiple lessons may look like the
following:

.. code-block:: yaml
    
  introduction-to-bits:
    min-age: 7
    max-age: 11
    number: 1
    programming-exercises:
      - count-to-16
      - count-to-1-million
    learning-outcomes:
      - binary-data-representation
    curriculum-areas*:
      - maths
    generated-resources:
      sorting-network:
        description: One per student.

  how-binary-digits-work:
    min-age: 7
    max-age: 11
    number: 2
    learning-outcomes:
      - binary-data-representation
      - binary-justify-representation


.. _learning-outcomes-file:

Learning Outcomes Configuration File
------------------------------------------------------------------------------

- **File Name:** ``learning-outcomes.yaml``

- **Location:** ``topics/content/<language>/``

- **Referenced In:** ``topics/content/<language>/structure.yaml``

- **Purpose:** Defines the learning outcomes avilable for all topics.

- **Required Fields:**

  - ``<key> : <value>`` Key value pairs. The key will be used in other configuration
    files to reference this particluar learning outcome. The value is the learning
    outcome text that will be displayed to the user).

A complete learning outcome structure file may look like the following:

.. code-block:: yaml

  binary-data-representation: Explain how a binary digit is represented using two contrasting values.
  binary-count: Demonstrate how to represent any number between 0 and 31 using binary.
  binary-convert-decimal: Perform a demonstration of how the binary number system works by converting any decimal number into a binary number.
  binary-justify-representation: Argue that 0’s and 1’s are still a correct way to represent what is stored in the computer.


.. _curriculum-areas-file:

Curriculum Areas Configuration File
------------------------------------------------------------------------------

- **File Name:** ``curriculum-areas.yaml``

- **Location:** ``topics/content/<language>/``

- **Referenced In:** ``topics/content/<language>/structure.yaml``

- **Purpose:** Defines the curriculum areas available for all topics.

- **Required Fields:**

  - ``<curriculum-area-name>:`` This is the key for the curriculum area. Each curriculum
    area has its own list of required and optional fields:

    - **Required Fields:**

      - ``name:`` The name of the curriculum area (this is what will be displayed to the
        user).

    - **Optional Fields:**

      - ``children:`` A list of sub-curriculum areas (see example file below). Each child
        requires a name field.

An example curriculum areas file with multiple curriculums may look like
the following:

.. code-block:: yaml

  maths:
    name: Maths
    children:
      geometry:
        name: Geometry
      algebra:
        name: Algebra

  science:
    name: Science

  art:
    name: Art

.. note::

  The maximum depth for children is one, that is, children curriculum areas
  cannot have children.

.. note::

  When including a curriculum area in another configuration file, adding a child
  curriculum area will automatically add the parent curriculum area, you do not need to
  specify this manually. For example, adding ``geometry`` means that ``maths`` is
  automatically included.


.. _programming-exercises-structure-file:

Programming Exercises Structure Configuration File
------------------------------------------------------------------------------

- **File Name:** ``programming-exercises-structure.yaml``

- **Location:** ``topics/content/<language>/``

- **Referenced In:** ``topics/content/<language>/structure.yaml``

- **Purpose:** This file defines the structure of programming exercises for all
  topics.

- **Required Fields:**

  - ``languages:`` A list of languages that programming exercises can be given in.

    - **Required Fields:**

      - ``<language-name>:`` This is the key for the language. Each language has its own
        list of required and optional fields:

        - **Required Fields:**

          - ``name:`` The name of the programming language (this is what will be
            displayed to the user).

        - **Optional Fields:**

          - ``icon:`` An image file to be used as the icon for the language.

  - ``difficulties:`` A list of difficulties programming exercises can be labelled as.

    - **Required Fields:**

      - ``<level>:`` An integer value.

        - **Required Fields:**

        - ``name:`` The name of the difficulty level (this is what will be displayed to
          the user).

A complete programming exercise structure file may look like the following:

.. code-block:: yaml

  language:
    scratch:
      name: Scratch
      icon: img/scratch-cat.png
    ruby:
      name: Ruby

  difficulties:
    1:
      name: Beginner
    2:
      name: Intermediate
    3:
      name: Advanced


.. _programming-exercises-file:

Programming Exercises Configuration File
------------------------------------------------------------------------------

- **File Name:** ``programming-exercises.yaml``

- **Location:** ``topics/content/<language>/<topic-name>/programming-exercises/``

- **Referenced In:** ``topics/content/<language>/<topic-name>/<topic-name>.yaml``

- **Purpose:** This file defines the programming exercises (and their respective attributes)
  for a particular topic.

- **Required Fields:**

  - ``<programming-exercise-name>``

    - **Required Fields:**

      - ``exercise-set-number:`` The group of related programming exercises this
        exercise belongs to.

      - ``exercise-number:`` The number order for this programming exercise.
        Exercises are sorted this number.

      - ``difficulty-level:`` A key corresponding to a difficulty level.

      - ``programming-languages:`` A list of keys corresponding to programming languages
        that this exercise is given in.

    - **Optional Fields:**

      - ``learning-outcomes:`` A list of keys corresponding to learning outcomes.

A complete programming exercises structure file may look like the following:

.. code-block:: yaml

  count-to-16:
    exercise-set-number: 1
    exercise-number: 1
    difficulty-level: 1
    programming-languages:
      - ruby
      - python
    learning-outcomes:
      - programming-sequence

  count-to-a-million:
    exercise-set-number: 1
    exercise-number: 2
    difficulty-level: 3
    programming-languages:
      - python
    learning-outcomes:
      - programming-basic-logic
    

.. _curriculum-integrations-file:

Curriculum Integrations Configuration File
------------------------------------------------------------------------------

- **File Name:** ``curriculum-intergrations.yaml``

- **Location:** ``topics/content/<language>/<topic-name>/``

- **Referenced In:** ``topics/content/<language>/<topic-name>.yaml``

- **Purpose:** Contains a list of curriculum integrations that can be used to integrate
  the topic with another area in the curriculum.

- **Required Fields:**

  - ``<curriculum-integration>:`` This is the key for the curriculum integration. Each
    curriculum integration has its own list of required and optional fields:

    - **Required Fields:**

      - ``number:`` The number order for this curriculum integration. Curriculum
        integrations are sorted by this number.

      - ``curriculum-areas:`` A list of keys corresponding to other curriculum areas
        that this curriculum integration could be used in.

    - **Optional Fields:**

      - ``prerequisite-lessons:`` A list of unit plan keys containing lessons that are
        expected to be completed before attempting this curriculum integration.

        - **Required Fields:**

          - ``<unit-plan-name>:`` A key corresponding to a unit plan.

            - **Required Fields:**

              - ``<lesson-name>`` A key corresponding to a lesson in the given unit
                plan.

A complete curriculum integration structure file with multiple curriculum integrations
may look like the following:

.. code-block:: yaml

  binary-number-bracelets:
    number: 1
    curriculum-areas:
      - math
      - art
    prerequisite-lessons:
      unit-plan:
        - introduction-to-binary-digits
      unit-plan-2:
        - counting-in-binary

  binary-leap-frog:
    number: 2
    curriculum-areas:
      - math
      - pe
    prerequisite-lessons:
      unit-plan-2:
        - counting-in-binary
