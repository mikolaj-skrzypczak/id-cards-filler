import hashlib
import os.path

from PIL import Image

from ids_filler import *
from ids_filler.attendess.attendees_loader import AttendeesLoader
from ids_filler.config import get_config, Config
from ids_filler.images.image_loader import ImageLoader
from ids_filler.images.image_modifier import ImageModifier

config: Config | None = None


def main():
    global config
    config = get_config()

    _clear_previous_results()

    for attendee_type, hex_color in config.get_attendees_types_and_corresponding_hex_colors():
        clear_card = ImageLoader.load_image(attendee_type)
        for attendee in AttendeesLoader.get_attendees_and_affiliations(attendee_type):
            card_to_fill = clear_card.copy()
            _fill_in_the_card(card_to_fill, attendee, hex_color)
            card_to_fill.save(f"{RESULTS_DIR}/{hashlib.md5(card_to_fill.tobytes()).hexdigest()}.png")


def _fill_in_the_card(card_to_fill: Image.Image, attendee: dict, hex_color: str) -> None:
    name, surname = attendee["name"].strip().title().rsplit(" ", 1)
    affiliation = attendee["affiliation"].strip()

    ImageModifier.insert_text(card_to_fill, name, NAME_FONT, hex_color, config.name_y_offset)
    ImageModifier.insert_text(card_to_fill, surname, NAME_FONT, hex_color, config.surname_y_offset)
    ImageModifier.insert_text(
        card_to_fill, affiliation, AFFILIATION_FONT, "#F4F4F4", config.affiliation_y_offset
    )


def _clear_previous_results() -> None:
    if os.path.exists(RESULTS_DIR):
        for file in os.listdir(RESULTS_DIR):
            os.remove(f"{RESULTS_DIR}/{file}")
    else:
        os.mkdir(RESULTS_DIR)


if __name__ == '__main__':
    main()
