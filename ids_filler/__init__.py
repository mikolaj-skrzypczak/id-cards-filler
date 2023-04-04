import os

from PIL import ImageFont

RESULTS_DIR = f"{os.path.dirname(__file__)}/results"

RESOURCES_DIR = f"{os.path.dirname(__file__)}/resources"
FONTS_DIR = f"{RESOURCES_DIR}/fonts"

NAME_FONT = ImageFont.truetype(font=f'{FONTS_DIR}/Rubik-Bold.ttf', size=100)
AFFILIATION_FONT = ImageFont.truetype(font=f'{FONTS_DIR}/Rubik-Bold.ttf', size=50)
