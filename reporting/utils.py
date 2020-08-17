
import os

from configparser import ConfigParser
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def get_project_config(config_file) -> ConfigParser:
    config = None

    config = ConfigParser()
    config.read_file(config_file)

    return config
