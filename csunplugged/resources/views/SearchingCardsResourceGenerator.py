"""Class for Searching Cards resource generator."""

from random import sample, shuffle
from math import ceil
from PIL import Image, ImageDraw, ImageFont
from yattag import Doc
from utils.BaseResourceGenerator import BaseResourceGenerator

IMAGE_PATH = "static/img/resources/searching-cards/{}-cards-{}.png"
X_BASE_COORD = 1803
X_COORD_DECREMENT = 516
Y_COORD = 240
FONT_PATH = "static/fonts/PatrickHand-Regular.ttf"
FONT = ImageFont.truetype(FONT_PATH, 200)


class SearchingCardsResourceGenerator(BaseResourceGenerator):
    """Class for Searching Cards resource generator."""

    additional_valid_options = {
        "number_cards": ["15", "31"],
        "max_number": ["cards", "99", "999", "blank"],
        "help_sheet": [True, False],
    }

    def data(self):
        """Create a image for Searching Cards resource.

        Returns:
            A list of dictionaries for each resource page.
        """
        pages = []
        number_cards = int(self.requested_options["number_cards"])
        max_number = self.requested_options["max_number"]
        help_sheet = self.requested_options["help_sheet"]

        if max_number == "cards":
            numbers = list(range(1, number_cards + 1))
            shuffle(numbers)
            range_text = "1 to {}".format(number_cards)
        elif max_number != "blank":
            numbers = sample(range(1, int(max_number) + 1), number_cards)
            range_text = "1 to {}".format(max_number)
        else:
            numbers = []
            range_text = "Add list of numbers below:"

        if help_sheet:
            pages.append({"type": "html", "data": self.create_help_sheet(numbers, range_text)})

        number_of_pages = range(ceil(number_cards / 4))
        for (page_number, page) in enumerate(number_of_pages):
            if page == number_of_pages[-1]:
                image_path = IMAGE_PATH.format(3, 1)
            else:
                image_path = IMAGE_PATH.format(4, page + 1)

            image = Image.open(image_path)

            if max_number != "blank":
                draw = ImageDraw.Draw(image)
                page_numbers = numbers[:4]
                numbers = numbers[4:]
                coord_x = X_BASE_COORD
                for number in page_numbers:
                    text = str(number)
                    text_width, text_height = draw.textsize(text, font=FONT)
                    draw.text(
                        (coord_x - (text_width / 2), Y_COORD - (text_height / 2)),
                        text,
                        font=FONT,
                        fill="#000"
                    )
                    coord_x -= X_COORD_DECREMENT

            image = image.rotate(90, expand=True)
            page_data = {"type": "image", "data": image}
            if page_number == 0:
                page_data["thumbnail"] = True
            pages.append(page_data)
        return pages

    def create_help_sheet(self, numbers, range_text):
        """Create helper sheet for resource.

        Args:
            numbers: Numbers used for activity (list).
            range_text: String describing range of numbers (str).

        Returns:
            Pillow image object (Image).
        """
        doc, tag, text, line = Doc().ttl()
        with tag("div"):
            with tag("h1"):
                text("Teacher guide sheet for binary search activity")
            with tag("p"):
                text(
                    "Use this sheet to circle the number you are asking your class ",
                    "to look for when you are demonstrating how the binary search ",
                    "works. This allows you to demonstrate the maximum number of ",
                    "searches it would take. When students are playing the treasure ",
                    "hunt game, they can choose any number. Avoid those numbers that are ",
                    "underlined as they are key binary search positions (avoiding them is a ",
                    "good thing to do for demonstrations, but in practice students, ",
                    "or computers, won’t intentionally avoid these)."
                )
            with tag("h2"):
                text("Sorted numbers")
            with tag("p"):
                # doc.attr(style="columns:2;")
                numbers.sort()
                red_number_jump = (len(numbers) + 1) // 4
                text = ""
                for (index, number) in enumerate(numbers):
                    if (index + 1) % red_number_jump == 0:
                        text += "<u>{}</u> - ".format(number)
                    else:
                        text += "{} - ".format(number)
                text = text[:-3]
                doc.asis(text)
        return doc.getvalue()

    @property
    def subtitle(self):
        """Return the subtitle string of the resource.

        Used after the resource name in the filename, and
        also on the resource image.

        Returns:
            text for subtitle (str).
        """
        max_number = self.requested_options["max_number"]
        help_sheet = self.requested_options["help_sheet"]
        number_cards = self.requested_options["number_cards"]

        if max_number == "blank":
            range_text = "blank"
        elif max_number == "cards":
            range_text = "0 to {}".format(number_cards)
        else:
            range_text = "0 to {}".format(max_number)

        if help_sheet:
            help_text = "with helper sheet"
        else:
            help_text = "without helper sheet"

        text = "{} cards - {} - {} - {}".format(
            number_cards,
            range_text,
            help_text,
            super().subtitle
        )
        return text
