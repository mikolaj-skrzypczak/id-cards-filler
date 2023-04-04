import os

import yaml


class Config:
    config_file = f"{os.path.dirname(os.path.abspath(__file__))}/config.yaml"

    def __init__(self):
        assert self._config_exists(), f'Config file ({self.config_file}) does not exist'
        self.config = self._load_config()

    def get_attendees_types_and_corresponding_hex_colors(self) -> tuple[str, str]:
        attendees = self.config.get('attendees', {})
        for type_, type_conf in attendees.items():
            yield type_, type_conf.get('color', '#000000')

    @property
    def name_y_offset(self) -> int:
        return self.config.get('name_y_offset', 850)

    @property
    def surname_y_offset(self) -> int:
        return self.config.get('surname_y_offset', 950)

    @property
    def affiliation_y_offset(self) -> int:
        return self.config.get('affiliation_y_offset', 1100)

    @classmethod
    def _load_config(cls) -> dict:
        with open(cls.config_file, 'r') as fp:
            return yaml.safe_load(fp)

    @classmethod
    def _config_exists(cls) -> bool:
        return os.path.exists(cls.config_file)
