import os
from typing import Union

from PIL import Image


class ImageLoader:
    clear_cards_dir = f"{os.path.dirname(__file__)}/../resources/clear_cards"

    @classmethod
    def load_image(cls, file_name: str) -> Union[Image.Image, None]:
        file_path = f"{cls.clear_cards_dir}/{file_name}.png"
        assert os.path.exists(file_path), f'File "{file_path}" does not exist'
        return Image.open(file_path)

    @classmethod
    def _clear_cards_dir_exists(cls) -> bool:
        return os.path.exists(cls.clear_cards_dir)
