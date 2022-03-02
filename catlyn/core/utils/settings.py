""" Settings module from CATlyn. hold logics for the setting class """
import json


class Settings():
    """
    This class is meant to be a wrapper around all possible instance settings
    """

    def __init__(self, config_path: str, secrets_path: str) -> None:
        self.config: dict = {}
        self.__config_path = config_path
        self.__secrets_path = secrets_path
        self.load_config(self.__config_path, self.__secrets_path)

    # * PRIVATE AND PROTECTED METHODS

    def __set_champion_datapath(self) -> None:
        """ sets champions datapath in self.config['data_paths'] """
        if not self.__secrets_path:
            return None
        champion_dp = self.config['data_paths']['champions'].replace("${language}", self.config['language'])
        self.config['data_paths']['champions'] = champion_dp

    # * PUBLIC METHODS

    def load_config(self, config_path: str = "", secrets_path: str = "") -> None:
        """ loads configurations from files """
        if not config_path:
            config_path = self.__config_path
        if not secrets_path:
            secrets_path = self.__secrets_path

        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
            print(">>> configurations Successfully loaded")
        with open(secrets_path, "r", encoding="utf-8") as f:
            secrets = json.load(f)
            print(">>> secrets Successfully loaded")

        self.config = {**config, **secrets}
        self.config['base_url'] = str(self.config['base_url']).replace("${region}", self.config['region'])
        self.__set_champion_datapath()
