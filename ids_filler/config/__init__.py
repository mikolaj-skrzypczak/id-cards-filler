from ids_filler.config.config import Config

_config: Config | None = None


def get_config():
    global _config
    if _config is None:
        _config = Config()
    return _config
