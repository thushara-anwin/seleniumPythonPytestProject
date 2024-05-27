import os
from configparser import ConfigParser


def read_configurations(category,key):
    config = ConfigParser()
    print(os.path.dirname(os.path.realpath(__file__)))
    config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'configurations\\config.ini')
    print(config_path)
    config.read(config_path)
    # config.read(r"configurations\config.ini")

    return config.get(category, key)