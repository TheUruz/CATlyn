from typing import Any, List
import requests

from catlyn.core.utils.settings import Settings
from catlyn.core.champion.champion import Champion
from catlyn.core.champion.champion_utils import get_champion_by_id


class ApiHandler():
    """ Class holding all the logic to interface with Riot API"""

    def __init__(self, settings: Settings) -> None:
        self.__settings = settings

    def _set_summoner_info(self, player_name: str) -> None:
        """ sets summoner info in configuration in passed in settings """
        if not player_name:
            return None
        self.__settings.config['summoner'] = self._get(f"/lol/summoner/v4/summoners/by-name/{player_name}")

    def _get(self, api_url: str) -> Any:
        """ generic GET HTTP call used in other class methods """
        if not check_url(api_url):
            api_url = self.__settings.config['base_url'] + api_url
        res = requests.get(api_url, headers={"X-Riot-Token": self.__settings.config['key']})
        data = res.json()
        return data

    def get_free_rotation(self, sort_by: str = "name") -> List[Champion]:
        """ get current week champion rotation """
        endpoint = "/lol/platform/v3/champion-rotations"
        data = self._get(api_url=endpoint)
        free_champs_ids = data['freeChampionIds']
        champ_rotation = []
        for champ_id in free_champs_ids:
            champ = get_champion_by_id(champ_id=str(champ_id), settings=self.__settings)
            champ_rotation.append((champ_id, champ["id"]))  # TODO continue here
        if sort_by == "id":
            champ_rotation.sort(key=lambda x: x[0])
        else:
            champ_rotation.sort(key=lambda x: x[1])
        return champ_rotation


def check_url(api_url: str) -> str:
    """ checks if passed in urls are relative or absolute """
    if api_url.startswith("http"):
        return api_url
    return ""
