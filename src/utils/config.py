from configparser import ConfigParser
from definitions import CONFIG_PATH
from definitions import ROOT_DIR

def get_config():
    config = ConfigParser()
    config.read_dict({'claimrank': {'project_path': ROOT_DIR}})
    config.read(CONFIG_PATH)
    return config['claimrank']
