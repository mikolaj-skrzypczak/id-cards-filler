import textwrap

from PIL import Image, ImageDraw
from PIL.ImageFont import FreeTypeFont


class ImageModifier:
    @classmethod
    def insert_text(
            cls,
            image: Image.Image,
            text: str,
            font: FreeTypeFont,
            text_color: str,
            text_start_height: int,
    ) -> None:
        lines = textwrap.wrap(text, width=40)

        cls._insert_text(image, lines, font, text_color, text_start_height)

    @staticmethod
    def _insert_text(
            image: Image.Image,
            lines: list[str],
            font: FreeTypeFont,
            text_color: str,
            text_start_height: int
    ) -> None:
        draw = ImageDraw.Draw(image)
        image_width, image_height = image.size
        y_text = text_start_height

        for line in lines:
            _, _, line_width, line_height = font.getbbox(line)
            draw.text(
                xy=((image_width - line_width) / 2, y_text),
                text=line,
                font=font,
                fill=text_color
            )
            y_text += line_height
