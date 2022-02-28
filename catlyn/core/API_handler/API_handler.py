"""Library for my custom Riot APIs"""

import json
from typing import Any, List, Union
import requests

# ENDPOINT = f"/lol/summoner/v4/summoners/by-name/{Riot.SUMMONER}"
# ENDPOINT = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{Riot.SUMMONER.get('puuid')}/ids?start=0&count=20"


class ApiHandler():
    """
    MY CUSTOM INTERFACE to RiotAPIs.\n
    All methods listed as public are meant to be the ones to be consumed. and/or overridden.
    All methods listed as private or protected should not be touched since they are used as utility from other methods inside the class.\n
    """

    def __init__(self) -> None:
        self.config: dict = {}

    # * PRIVATE AND PROTECTED METHODS

    def __set_summoner_info(self, player_name: str) -> None:
        """ sets summoner info in self.config"""
        if not player_name:
            return None
        self.config['summoner'] = self.get(f"/lol/summoner/v4/summoners/by-name/{player_name}")

    def __set_champion_datapath(self, champion_dp: str) -> None:
        """ sets champions datapath in self.config['data_paths'] """
        champion_dp = champion_dp.replace("${language}", self.config['language'])
        self.config['data_paths']['champions'] = "../" + champion_dp

    def __forge_url(self, api_url: str) -> str:
        """ adds base url to API urls if needed """
        if api_url.startswith("http"):
            return api_url
        else:
            return self.config['base_url'] + api_url

    def _get_champion_name(self, champ_id: Union[int, str]) -> str:
        """ returns champion name based on provided id """
        if isinstance(champ_id, int):
            champ_id = str(champ_id)

        path = self.config["data_paths"]["champions"] + "/championFull.json"

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            champ_map = data.get("keys")
            champ_name = champ_map.get(champ_id)
            return champ_name

    # * PUBLIC METHODS

    def load_config(self, config_path: str, secrets_path: str) -> None:
        """ loads configurations from files """
        # ? load CONFIG
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
            print(">>> configurations Successfully loaded")
        # ? load SECRETS
        with open(secrets_path, "r", encoding="utf-8") as f:
            secrets = json.load(f)
            print(">>> secrets Successfully loaded")
        self.config = {**config, **secrets}
        self.config['base_url'] = str(self.config['base_url']).replace("${region}", self.config['region'])
        self.__set_champion_datapath(self.config['data_paths']['champions'])
        self.__set_summoner_info(self.config['summoner'])

    def get(self, api_url: str) -> Any:
        """ make an HTTP GET to Riot API """
        api_url = self.__forge_url(api_url)
        res = requests.get(api_url, headers={
                           "X-Riot-Token": self.config['key']})
        data = res.json()
        return data

    def get_champion_info(self, champ_name: str = "", champ_id: Union[int, str] = "") -> dict:
        """This method returns a dict object containing all of its informations

        Args:
            champ_name (str, optional): name of the champion you are looking for. Defaults to "".
            champ_id (Union[int, str], optional): numeric id of the champion you are looking for. Defaults to "".

        Raises:
            Exception: raised when either champ_name or champ_id are passed

        Returns:
            dict: all infos about the desired champion
        """

        if (not champ_name and not champ_id) or (not champ_name and not str(champ_id).isdigit()):
            raise Exception("Cannot look for a champion without champ_name or champ_id")

        if not champ_name:
            champ_name = self._get_champion_name(champ_id=champ_id)

        path = f"{self.config['data_paths']['champions']}/champion/{champ_name}.json"

        with open(path, "r", encoding="utf-8") as f:
            champ_data = json.load(f)
            return champ_data

    def get_free_rotation(self, sort_by: str = "name") -> List[tuple]:
        """ get current week rotation """
        endpoint = "/lol/platform/v3/champion-rotations"
        data = self.get(api_url=endpoint)
        free_champs_ids = data['freeChampionIds']
        champ_rotation = []
        for champ_id in free_champs_ids:
            champ_name = self._get_champion_name(champ_id)
            champ_rotation.append((champ_id, champ_name))
        if sort_by == "id":
            champ_rotation.sort(key=lambda x: x[0])
        else:
            champ_rotation.sort(key=lambda x: x[1])
        return champ_rotation
