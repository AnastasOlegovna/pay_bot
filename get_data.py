import yaml
from pathlib import Path
import os
from os.path import join, dirname
from dotenv import load_dotenv


def get_from_env(key):
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)  # возвращен серкетный токен (или ключ к платежной системе)


file_name = "config.yaml"
script_path = Path(__file__).parent
config_file = script_path / file_name


def read_config():
    try:
        with open(config_file) as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        logger.error('Configuration file not found!')
        return None


# Initial setup
config = read_config()
