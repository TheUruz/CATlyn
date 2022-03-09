"""Contains the Catlyn class which is CATlyn entry point"""
from typing import Any
import requests

from catlyn.config import settings as _settings
from catlyn.core.champion import champion as _champion
from catlyn.shared import (
    utils as _utils,
    errors as _err
)


class Catlyn():
    """CATlyn entry point. This class holds all the interface logic with Riot API"""

    def __init__(self, settings: _settings.Settings) -> None:
        self.__settings = settings

    # * PRIVATE AND PROTECTED METHODS
    def _set_summoner_info(self, player_name: str) -> None:
        """ sets summoner info in configuration in passed in settings """
        if not player_name:
            return None
        self.__settings.config['summoner'] = self._get(f"/lol/summoner/v4/summoners/by-name/{player_name}")

    def _get(self, api_url: str) -> Any:
        """ generic GET HTTP call used in other class methods """
        if not _utils.check_url(api_url):
            api_url = self.__settings.config['base_url'] + api_url
        res = requests.get(api_url, headers={"X-Riot-Token": self.__settings.config['key']})
        data = res.json()
        return data

    # * PUBLIC METHODS
    def get_free_rotation(self, sort_by: str = "name") -> list[tuple]:
        """ get current week's champion rotation """
        endpoint = "/lol/platform/v3/champion-rotations"
        data = self._get(api_url=endpoint)
        try:
            free_champs_ids = data['freeChampionIds']
        except KeyError as err:
            raise _err.RiotKeyExpired from err
        champ_rotation = []
        for champ_id in free_champs_ids:
            champ = self.get_champion_by_id(champ_id=str(champ_id))
            champ_rotation.append((champ.key, champ.name))
        if sort_by == "id":
            champ_rotation.sort(key=lambda x: x[0])
        elif sort_by == "name":
            champ_rotation.sort(key=lambda x: x[1])
        return champ_rotation

    def get_champion_by_name(self, champ_name: str) -> _champion.Champion:
        """Retrieve a champion object from a champion name

        Args:
            champ_name (str): the name of the champion (case sensitive)
            settings (Settings): a setting object used to retrieve data_paths 

        Returns:
            Champion: a Champion object with all champion informations
        """
        full_data = _utils.get_champion_file(self.__settings)
        try:
            champ_data = full_data["data"][champ_name]
        except KeyError as err:
            raise _err.MissingChampName(champ_name) from err

        champ_data = _champion.Champion(champ_data)
        return champ_data

    def get_champion_by_id(self, champ_id: str) -> _champion.Champion:
        """Retrieve champion object from champion id

        Args:
            champ_id (str): the numeric id of the champion
            settings (Settings): a setting object used to retrieve data_paths 

        Returns:
            Champion: a Champion object with all champion informations
        """
        assert champ_id.isdigit(), ValueError("champ_id must be digit")
        champ_id = str(champ_id)
        full_data = _utils.get_champion_file(self.__settings)
        try:
            champ_name = full_data["keys"][champ_id]
        except KeyError as err:
            raise _err.MissingChampId(champ_id) from err
        champ_data = self.get_champion_by_name(champ_name=champ_name)
        return champ_data
