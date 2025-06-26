import configparser
import os

def readConfigData(section, key):
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_path, "ConfigurationFiles", "Config.cfg")
    cfg = configparser.ConfigParser()
    cfg.read(config_path)
    return cfg.get(section, key)

def readElementLocators(section, key):
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(base_path, "ConfigurationFiles", "Elements.cfg")
    cfg = configparser.ConfigParser()
    cfg.read(config_path)
    return cfg.get(section, key)