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

      - A **lesson** can contain **learning outcomes**, and
        **generated resources**.

  - A **topic** can also contain **curriculum integrations**, which can also contain
    **curriculum areas**.

  - A **topic** can also contain **programming challenges**.

    - A **programming challenge** can use different **programming languages**, and be set at
      a specific **difficulty**.

- **Learning outcomes**, **curriculum areas**, **glossary definitions**,
  **programming languages**, and **programming challenge difficulties** are
  defined at a language level, so can be used by all topic content
  of that language.

This is just a broad overview of the topics application.

Viewing All Topics Content
------------------------------------------------------------------------------

When developing locally, once you have run ``./csu start`` (see
:doc:`../getting_started/helper_commands`) you can go to the url below to get a
quick overview of what content is loaded:

.. code-block:: none

  localhost/__dev__/

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

.. _adding-a-topic:

Adding a Topic
------------------------------------------------------------------------------

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. The image is included as raw HTML because it has clickable nodes.
.. raw:: html

  <map name="topics-map">
    <area shape="rect" coords="240,308,317,343" href="#topic-configuration-file">
    <area shape="rect" coords="240,410,317,445" href="#application-structure-configuration-file">
    <area shape="rect" coords="240,513,317,550" href="#adding-a-unit-plan">
    <area shape="rect" coords="240,615,317,650" href="../getting_started/helper_commands.html#update">
  </map>
  <img src="../_static/img/topics_adding_topic_flowchart.png" usemap="#topics-map">

The Markdown file containing the description of the topic:

- **Is in:** the topic directory, e.g. the description file for
  Binary Numbers will be in ``topics/content/en/binary-numbers/``.
- **Is called:** ``<topic-key>.md`` where ``<topic-key>`` is the key
  (:ref:`what-is-a-key`) of the topic and the name of the directory it is in,
  e.g. ``binary-numbers.md`` or ``kidbots.md``.
- **Contains:** An H1 heading (i.e. has a single ``#`` prefix) and the content
  of the description.

.. note ::

  The heading written in this file will be used exactly as it is given
  throughout the website as the name of the topic.

.. warning::

  Every topic needs at least one unit plan, therefore the system will not allow
  a topic to be loaded until a unit plan is connected to it.

.. _adding-a-unit-plan:

Adding a Unit Plan
------------------------------------------------------------------------------

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. The image is included as raw HTML because it has clickable nodes.
.. raw:: html

  <map name="unit-plan-map">
    <area shape="rect" coords="240,435,317,468" href="#unit-plan-configuration-file">
    <area shape="rect" coords="240,547,317,581" href="#unit-plan-configuration-file">
    <area shape="rect" coords="240,658,317,692" href="#topic-configuration-file">
    <area shape="rect" coords="240,758,317,792" href="#adding-a-lesson">
    <area shape="rect" coords="240,864,317,896" href="../getting_started/helper_commands.html#update">
  </map>
  <img src="../_static/img/topics_adding_unit_plan_flowchart.png" usemap="#unit-plan-map">

The Markdown file containing the content og the unit plan:

- **Is in:** the unit plan directory, e.g. the unit plan file for Binary Numbers
  Unit Plan 2 will be in ``topics/content/en/binary-numbers/unit-plan-2/``.
- **Is called:** ``<unit-plan-key>.md`` where ``<unit-plan-key>`` is the key
  (:ref:`what-is-a-key`) of the unit plan and the name of the directory it is
  in, e.g. ``unit-plan-2.md``.
- **Contains:** An H1 heading (i.e. has a single ``#`` prefix) and the content
  of the unit plan.

.. note::

  The heading written in this file will be used exactly as it is given
  throughout the website as the name of the unit plan.

.. warning::

  Every unit plan needs at least one lesson, so the system will not allow a
  unit plan to be loaded until a lesson is connected to it.

.. _adding-a-lesson:

Adding a Lesson
------------------------------------------------------------------------------

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. The image is included as raw HTML because it has clickable nodes.
.. raw:: html

  <map name="lesson-map">
    <area shape="rect" coords="238,318,315,351" href="#lesson-configuration-file">
    <area shape="rect" coords="237,431,317,465" href="#lesson-configuration-file">
    <area shape="rect" coords="237,534,317,569" href="#unit-plan-configuration-file">
    <area shape="rect" coords="237,638,317,671" href="../getting_started/helper_commands.html#update">
  </map>
  <img src="../_static/img/topics_adding_lesson_flowchart.png" usemap="#lesson-map">

The Markdown file containing the content for the lesson:

- **Is in:** the lesson subdirectory in the unit plan directory, e.g.
  ``topics/content/en/binary-numbers/unit-plan/lessons/``.
- **Is called:** ``<lesson-key>.md`` where ``<lesson-key>`` is the key
  (:ref:`what-is-a-key`) of the lesson, e.g. ``introduction-to-bits.md``.
- **Contains:** An H1 heading (i.e. has a single ``#`` prefix) and the content
  for the lesson.

.. note::

  The heading written in this file will be used exactly as it is given
  throughout the website as the name of the lesson.

.. note::

  If a lesson includes programming challenges, Computational Thinking links,
  and/or learning outcomes, then the corresponding configuration and content
  files may also need to be added or updated.

.. _adding-learning-outcomes:

Adding Learning Outcomes
------------------------------------------------------------------------------

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. The image is included as raw HTML because it has clickable nodes.
.. raw:: html

  <map name="learning-outcomes-map">
    <area shape="rect" coords="240,100,317,135" href="#learning-outcomes-configuration-file">
    <area shape="rect" coords="240,210,317,245" href="#application-structure-configuration-file">
    <area shape="rect" coords="555,200,633,235" href="#learning-outcomes-configuration-file">
    <area shape="rect" coords="240,330,317,362" href="../getting_started/helper_commands.html#update">
  </map>
  <img src="../_static/img/topics_adding_learning_outcomes_flowchart.png" usemap="#learning-outcomes-map">

You will now be able to add learning outcomes to lessons and programming
challenges by referencing the keys you specified in the learning outcomes configuration
file.

.. note::

  If a learning outcome contains curriculum areas, then the curriculum areas
  configuration file may also need to be added or updated.

.. _adding-curriculum-areas:

Adding Curriculum Areas
------------------------------------------------------------------------------

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. The image is included as raw HTML because it has clickable nodes.
.. raw:: html

  <map name="curriculum-areas-map">
    <area shape="rect" coords="240,100,317,135" href="#curriculum-areas-configuration-file">
    <area shape="rect" coords="240,210,317,245" href="#application-structure-configuration-file">
    <area shape="rect" coords="560,200,642,232" href="#curriculum-areas-configuration-file">
    <area shape="rect" coords="240,330,317,362" href="../getting_started/helper_commands.html#update">
  </map>
  <img src="../_static/img/topics_adding_curriculum_areas_flowchart.png" usemap="#curriculum-areas-map">

You will now be able to add curriculum areas to learning outcomes and curriculum
integrations by referencing the keys you specified in the curriculum areas
configuration file.

.. _adding-a-programming-challenge:

Adding a Programming Challenge
------------------------------------------------------------------------------

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. The image is included as raw HTML because it has clickable nodes.
.. raw:: html

  <map name="programming-challenges-map">
    <area shape="rect" coords="554,470,633,505" href="#programming-challenges-configuration-file">
    <area shape="rect" coords="240,572,317,605" href="#programming-challenges-configuration-file">
    <area shape="rect" coords="240,694,317,727" href="#topic-configuration-file">
    <area shape="rect" coords="240,833,317,867" href="#programming-challenges-structure-configuration-file">
    <area shape="rect" coords="240,995,317,1030" href="../getting_started/helper_commands.html#update">
  </map>
  <img src="../_static/img/topics_adding_programming_challenges_flowchart.png" usemap="#programming-challenges-map">

You will now be able to add programming challenges to lessons by referencing the
keys you specified in the programming challenges configuration file.

A programming challenge is split into several different sections, each of which
is an its own Markdown file, all of which are in
``topics/content/en/binary-numbers/programming-challenges/<challenge-key>/``
where ``<challenge-key>`` refers to the key (:ref:`what-is-a-key`) of the
challenge, e.g. ``count-to-16``.

    1. The challenge description:

      - **Is called:** ``<challenge-key>.md`` where ``<challenge-key>`` is the key
        of the challenge, e.g. ``count-to-16.md``.
      - **Contains:** An H1 heading (i.e. has a single ``#`` prefix) and the content
        of the challenge.

      .. note::

        The heading written in this file will be used exactly as it is given
        throughout the website as the name of the programming challenge.

    2. The expected output

      - **Is called:** ``<language>-expected.md`` where ``<language>`` is the key
        of the programming language, e.g. ``python-expected.md``.
      - **Contains:** The expected output for the programming challenge, e.g. an
        embedded Scratch program or Python output.

    3. Hints (optional)

      - **Is called:** ``<language>-hints.md`` where ``<language>`` is the key
        of the programming language, e.g. ``scratch-hints.md``.
      - **Contains:** Hints for how to complete the challenge, e.g. suggested
        Scratch blocks.

    4. Example solution(s)

      - **Is called:** ``<language>-solution.md`` where ``<language>`` is the key
        of the programming language, e.g. ``ruby-solution.md``.
      - **Contains:** Example solutions to the challenge, e.g. Scratch program.

    5. Extra challenge(s) (optional)

      - **Is called:** the value defined in the programming challenges
        configuration file.
        A common filename is ``extra-challenge.md``.
      - **Contains:** Content for an extra challenge.

2-4 from the list above can be given in multiple programming languages.
Therefore, the languages you have chosen must be specified in the
``programming-challenges.yaml`` configuration file, as well as the
``programming-challenges-structure.yaml`` configuration file.

.. note::

  If the challenge includes learning outcomes, then the corresponding configuration
  file will also need to be added or updated to include new learning outcomes.

.. _adding-a-curriculum-integration:

Adding a Curriculum Integration
------------------------------------------------------------------------------

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. The image is included as raw HTML because it has clickable nodes.
.. raw:: html

  <map name="curriculum-integrations-map">
    <area shape="rect" coords="568,350,645,385" href="#curriculum-integrations-configuration-file">
    <area shape="rect" coords="240,450,317,485" href="#curriculum-integrations-configuration-file">
    <area shape="rect" coords="240,565,317,600" href="#topic-configuration-file">
    <area shape="rect" coords="240,675,317,710" href="../getting_started/helper_commands.html#update">
  </map>
  <img src="../_static/img/topics_adding_curriculum_integrations_flowchart.png" usemap="#curriculum-integrations-map">

The Markdown file containing the content of the curriculum integration:

- **Is in:** the curriculum integration directrory, e.g. curriculum integrations
  in Binary Numbers will be in
  ``topics/content/en/binary-numbers/curriculum-integrations/``.
- **Is called:** ``<integration-key>.md`` where ``<integration-key>`` is the key
  (:ref:`what-is-a-key`) of the curriculum integration, e.g. ``whose-cake-is-it.md``.
- **Contains:** An H1 heading (i.e. has a single ``#`` prefix) and the content
  of the integration.

.. note ::

  If the integration includes curriculum areas and/or prerequisite lessons,
  then the corresponding configuration and content files will also need to be added.

.. _adding-glossary-definitions:

Adding Glossary Definitions
------------------------------------------------------------------------------

.. The following image can copied for be edits here: https://goo.gl/Vjv6XV
.. The image is included as raw HTML because it has clickable nodes.
.. raw:: html

  <map name="glossary-definitions-map">
    <area shape="rect" coords="240,110,317,145" href="#application-structure-configuration-file">
    <area shape="rect" coords="240,320,320,350" href="#glossary-definitions-markdown-file">
    <area shape="rect" coords="240,430,319,462" href="../getting_started/helper_commands.html#update">
  </map>
  <img src="../_static/img/topics_adding_glossary_definitions_flowchart.png" usemap="#glossary-definitions-map">

.. _glossary-definitions-markdown-file:

Each glossary definition requires a Markdown file within the glossary
folder, with the filename as the glossary key.
When linking text to a glossary definition, the key is used as the identifier.
For example, with the key ``pixel``, then a file ``pixel.md`` is
expected.

Each Markdown file should start with a heading containing the glossary term
(this should be capitalized and include any required punctuation), followed
by the term's definition.

Continuing the ``pixel.md`` example from above, this could be the possible
contents of that file.

.. code-block:: none

    # Pixel

    This term is an abbreviation of picture element, the name given to the
    tiny squares that make up a grid that is used to represent images on a
    computer.

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

  - Some of the keys (:ref:`what-is-a-key`) have angle brackets around them,
    ``<like so>``. This means that they are variables and you can call them
    whatever you like in your configuration file (without the angle brackets).

.. _application-structure-file:

Application Structure Configuration File
------------------------------------------------------------------------------

- **File Name:** ``structure.yaml``

- **Location:** ``topics/content/<language>/``

- **Purpose:** Defines the top level configuration files to process for defining
  the content of the topics application.

- **Required Fields:**

  - ``topics:`` A list of file paths to topic configuration files.

- **Optional Fields:**

    - ``learning-outcomes:`` The path to the learning outcomes configuration file.
    - ``curriculum-areas:`` The path to the curriculum areas configuration file.
    - ``programming-challenges-structure:`` The path to the programming exercies structure
      configuration file.
    - ``glossary-folder:`` The folder name that contains the Markdown files for
      glossary definitions.

A complete application structure file may look like the following:

.. code-block:: yaml

  topics:
    - binary-numbers
    - error-detection-correction

  learning-outcomes: learning-outcomes.yaml
  curriculum-areas: curriculum-areas.yaml
  programming-challenges-structure: programming-challenges-structure.yaml

  glossary-folder: glossary

.. _topic-file:

Topic Configuration File
------------------------------------------------------------------------------

- **File Name:** ``<topic-key>.yaml``

- **Location:** ``topic/content/<language>/<topic-key>/``

- **Referenced In:** ``topic/content/<launguage>/structure.yaml``

- **Purpose:** This file defines the attributes of a specific topic, including connected
  unit plan, programming challenge, and curriculum integration configuration files.

- **Required Fields:**

  - ``unit-plans:`` A list of keys, where each key is a unit plan.

- **Optional Fields:**

  - ``icon:`` An image file to be used as the icon for the topic.

  - ``other-resources:`` A Markdown file containing information about other related
    (external) resources.

  - ``programming-challenges:`` The path to the programming challenges configuration file.

  - ``curriculum-integrations:`` The path to the curriculum integrations configuration
    file.

A complete topic structure file may look like the following:

.. code-block:: yaml

  unit-plans:
    - unit-plan
    - unit-plan-2

  icon: img/binary-numbers-0-1.png

  other-resources: other-resources.md

  programming-challenges: programming-challenges/programming-challenges.yaml
  curriculum-integrations: curriculum-integrations/curriculum-integrations.yaml

.. _unit-plan-file:

Unit Plan Configuration File
------------------------------------------------------------------------------

- **File Name:** ``<unit-plan-key>.yaml``

- **Location:** ``topic/content/<language>/<topic-key>/<unit-plan-key>/``

- **Referenced In:** ``topic/content/<language>/<topic-key>/<topic-key>.yaml``

- **Purpose:** This file defines which lessons to use in each age group

  - **Required Fields:**

    - ``lessons:`` The path to the lessons configuration file.

    - ``age-groups:`` Keys of age groups and their corresponding lessons.

      - **Required Fields:**

        - ``<age-group>:`` The key for the age group.

          - **Required Fields:**

            - ``<lesson-key>`` The key for a lesson.

              - **Required Fields:**

                - ``number`` The number order for this lesson, relative
                  to this age group.
                  This value allows a lesson to be used in different age
                  groups, as different numbered lessons (e.g. lesson 2 for
                  5 to 7, but lesson 1 for 8 to 10).

  - **Optional Fields:**

    - ``computational-thinking-links``: The Markdown filename containing
        Computational Thinking links.

A complete unit plan structure file with multiple lessons may look like the
following:

.. code-block:: yaml

  lessons: lessons/lessons.yaml

  age-groups:
    5-7:
      what-is-binary-junior:
        number: 1
      how-binary-digits-work:
        number: 2
    8-10:
      how-binary-digits-work:
        number: 1
      reinforcing-sequencing-in-binary-number-systems:
        number: 2
      codes-for-letters-using-binary-representation:
        number: 3


Lesson Configuration File
------------------------------------------------------------------------------

- **File Name:** ``<lessons>.yaml``

- **Location:** ``topic/content/<language>/<topic-key>/<unit-plan-key>/lessons/``

- **Referenced In:** ``topic/content/<language>/<topic-key>/<unit-plan-key>/<unit-plan-key>.yaml``

- **Purpose:** This file defines all the lessons (and their respective)
  attributes for the unit plan.

  - **Required Fields:**

    - ``<lesson-key>:`` This is the key for the lesson. Each lesson has its own list of
      required and optional fields:

      - **Optional Fields:**

        - ``duration``: The estimated time to complete the lesson (in minutes).

        - ``computational-thinking-links``: The Markdown filename containing
          Computational Thinking links.

        - ``programming-challenges:`` A list of keys corresponding to programming
          challenges.

        - ``programming-challenges-description``: The Markdown filename
          containing a description for the programming challenges.

        - ``learning-outcomes:`` A list of keys corresponding to learning outcomes.

        - ``classroom-resources:`` A list of strings describing the required
          classroom resources.
          The list items must be short (less than 100 characters),
          as this list is displayed on the lesson sidebar.
          If a longer description is required, this should be within the lesson
          text within a panel.

        - ``generated-resources:`` A list of generated CSU resources connected to this
          lesson.

          - **Required Fields:**:

            - ``<resource>``: The key corresponding to the resource.

              - **Required Fields:**:

                - ``description:`` A description of how the resource should be used.

A complete lesson structure file with multiple lessons may look like the
following:

.. code-block:: yaml

  introduction-to-bits:
    programming-challenges:
      - count-to-16
      - count-to-1-million
    learning-outcomes:
      - binary-data-representation
    generated-resources:
      sorting-network:
        description: One per student.
    classroom-resources:
      - Pens and paper
      - Dice

  how-binary-digits-work:
    computational-thinking-links: how-binary-digits-work-ct-links.md
    learning-outcomes:
      - binary-data-representation
      - binary-justify-representation

.. _age-groups-file:

Age Group Configuration File
------------------------------------------------------------------------------

- **File Name:** ``age-groups.yaml``

- **Location:** ``topics/content/<language>/``

- **Referenced In:** ``topics/content/<language>/structure.yaml``

- **Purpose:** Defines the age groups avilable for all lessons.

- **Required Fields:**

  - ``<age-group-key>:`` This is the key for the age group.
    Each age group has its own list of required and optional fields:

    - **Required Fields:**

      - ``min_age:`` The minimum age of the age group.
      - ``max_age:`` The maximum age of the age group.

    - **Optional Fields:**

      - ``description:`` A text description for the age group.

A complete age group structure file may look like the following:

.. code-block:: yaml

  5-7:
      min_age: 5
      max_age: 7
      description: In the teacher observations sections there may also be background notes on the big picture. There is no expectation that 5 to 7 year olds will need to know this, but if you are asked, you have the answer at your fingertips.
  8-10:
      min_age: 8
      max_age: 10
  11-14:
      min_age: 11
      max_age: 14

.. _learning-outcomes-file:

Learning Outcomes Configuration File
------------------------------------------------------------------------------

- **File Name:** ``learning-outcomes.yaml``

- **Location:** ``topics/content/<language>/``

- **Referenced In:** ``topics/content/<language>/structure.yaml``

- **Purpose:** Defines the learning outcomes avilable for all topics.

- **Required Fields:**

  - ``<learning-outcome-key>:`` This is the key for the learning outcome.
    Each learning outcome has its own list of required and optional fields:

    - **Required Fields:**

      - ``text:`` The text of the learning outcome (this is what will
        be displayed to the user).

    - **Optional Fields:**

      - ``curriculum-areas:`` A list of curriculum area key (see example file below).

A complete learning outcome structure file may look like the following:

.. code-block:: yaml

  no-physical-zeros-ones:
    text: Justify why there aren’t actual 0’s and 1’s zooming around inside a computer.
    curriculum-areas:
      - computational-thinking

  binary-correct-representation:
    text: Argue that 0’s and 1’s are still a correct way to represent what is stored in the computer.
    curriculum-areas:
      - computational-thinking
      - data-representation

  maths-comparing-numbers:
    text: Compare numbers
    curriculum-areas:
      - numeracy

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
      - ``number:`` A number used for ordering curriculum areas.
        Areas are sorted in ascending numbers (smallest to largest).
      - ``colour:`` The CSS colour class to use for colouring the curriculum
        area badge on the website.
        This colour is also applied to all children of curriculum area.

        Available colours include:

        - ``blue``
        - ``green``
        - ``light-purple``
        - ``orange``
        - ``pink``
        - ``purple``
        - ``red``
        - ``teal``
        - ``yellow``

        These colours are defined in: ``csunplugged/static/scss/website.scss``.

    - **Optional Fields:**

      - ``children:`` A list of sub-curriculum areas (see example file below). Each child
        requires a ``name`` field.
        Children inherit the same colour and number as their parent.

An example curriculum areas file with multiple curriculums may look like
the following:

.. code-block:: yaml

  maths:
    name: Maths
    colour: green
    children:
      geometry:
        name: Geometry
      algebra:
        name: Algebra

  science:
    name: Science
    colour: blue

  art:
    name: Art
    colour: teal

.. note::

  The maximum depth for children is one, that is, children curriculum areas
  cannot have children.

.. note::

  When including a curriculum area in another configuration file, adding a child
  curriculum area will automatically add the parent curriculum area, you do not need to
  specify this manually. For example, adding ``geometry`` means that ``maths`` is
  automatically included.

.. _programming-challenges-structure-file:

Programming Challenges Structure Configuration File
------------------------------------------------------------------------------

- **File Name:** ``programming-challenges-structure.yaml``

- **Location:** ``topics/content/<language>/``

- **Referenced In:** ``topics/content/<language>/structure.yaml``

- **Purpose:** This file defines the structure of programming challenges for all
  topics.

- **Required Fields:**

  - ``languages:`` A list of languages that programming challenges can be given in.

    - **Required Fields:**

      - ``<language-name>:`` This is the key for the language. Each language has its own
        list of required and optional fields:

        - **Required Fields:**

          - ``name:`` The name of the programming language (this is what will be
            displayed to the user).

          - ``number:`` A number used for ordering programming languages.
            Languages are sorted in ascending numbers (smallest to largest).

        - **Optional Fields:**

          - ``icon:`` An image file to be used as the icon for the language.

  - ``difficulties:`` A list of difficulties programming challenges can be labelled as.

    - **Required Fields:**

      - ``<level>:`` An integer value.

        - **Required Fields:**

        - ``name:`` The name of the difficulty level (this is what will be displayed to
          the user).

A complete programming challenge structure file may look like the following:

.. code-block:: yaml

  language:
    scratch:
      name: Scratch
      number: 1
      icon: img/scratch-cat.png
    ruby:
      name: Ruby
      number: 2

  difficulties:
    1:
      name: Beginner
    2:
      name: Intermediate
    3:
      name: Advanced

.. _programming-challenges-file:

Programming Challenges Configuration File
------------------------------------------------------------------------------

- **File Name:** ``programming-challenges.yaml``

- **Location:** ``topics/content/<language>/<topic-key>/programming-challenges/``

- **Referenced In:** ``topics/content/<language>/<topic-key>/<topic-key>.yaml``

- **Purpose:** This file defines the programming challenges (and their respective attributes)
  for a particular topic.

- **Required Fields:**

  - ``<programming-challenge-name>``

    - **Required Fields:**

      - ``challenge-set-number:`` The group of related programming challenges this
        challenge belongs to (see note below).

      - ``challenge-number:`` The number order for this programming challenge (see note below).

      - ``difficulty-level:`` A key corresponding to a difficulty level.

      - ``programming-languages:`` A list of keys corresponding to programming languages
        that this challenge is given in.

    - **Optional Fields:**

      - ``learning-outcomes:`` A list of keys corresponding to learning outcomes.

      - ``extra-challenge:`` A Markdown filename containing the content for an
        extra challenge.

.. note ::

  Programming challenges are sorted by their ``challenge-set-number``
  and then their ``challenge-number``.
  These numbers are not directly displayed, but used to calculate a
  programming challenge's number for a lesson.

  For example, if a lesson lists the following challenges:

  - Challenge A: 1.1
  - Challenge B: 1.3
  - Challenge C: 2.2
  - Challenge D: 9.3

  The lesson will display these challenges as:

  - Challenge A: 1.1
  - Challenge B: 1.2
  - Challenge C: 2.1
  - Challenge D: 3.1

A complete programming challenges structure file may look like the following:

.. code-block:: yaml

  count-to-16:
    challenge-set-number: 1
    challenge-number: 1
    difficulty-level: 1
    programming-languages:
      - ruby
      - python
    learning-outcomes:
      - programming-sequence

  count-to-a-million:
    challenge-set-number: 1
    challenge-number: 2
    difficulty-level: 3
    programming-languages:
      - python
    learning-outcomes:
      - programming-basic-logic
    extra-challenge: extra-challenge.md

.. _curriculum-integrations-file:

Curriculum Integrations Configuration File
------------------------------------------------------------------------------

- **File Name:** ``curriculum-intergrations.yaml``

- **Location:** ``topics/content/<language>/<topic-key>/``

- **Referenced In:** ``topics/content/<language>/<topic-key>.yaml``

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

          - ``<unit-plan-key>:`` A key corresponding to a unit plan.

            - **Required Fields:**

              - ``<lesson-key>`` A key corresponding to a lesson in the given unit
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
