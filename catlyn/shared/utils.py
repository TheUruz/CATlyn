"""Utility classes and functions"""
#! watch out for circular imports since this module is meant to be imported by many packages

import json
from catlyn.shared import errors as _err
from catlyn.config import settings as _settings
from catlyn.core.champion import champion as _champion

# ENDPOINT = f"/lol/summoner/v4/summoners/by-name/{Riot.SUMMONER}"
# ENDPOINT = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{Riot.SUMMONER.get('puuid')}/ids?start=0&count=20"


def get_champion_file(settings: _settings.Settings) -> dict:
    """Retrieve championFull.json file data

    Args:
        settings (Settings): setting object from which retrieve data paths

    Returns:
        dict: json object containing all champions informations from data dragon
    """
    path = settings.config['data_paths']['champions']

    with open(path, "r", encoding="utf-8") as f:
        champ_data = json.load(f)
        return champ_data


def get_champion_by_name(champ_name: str, settings: _settings.Settings) -> _champion.Champion:
    """Retrieve champion object from a champion name

    Args:
        champ_name (str): the name of the champion (case sensitive)
        settings (Settings): a setting object used to retrieve data_paths 

    Returns:
        Champion: a Champion object with all champion informations
    """
    full_data = get_champion_file(settings)
    try:
        champ_data = full_data["data"][champ_name]
    except KeyError as err:
        raise _err.MissingChampName(champ_name) from err
    return champ_data


def get_champion_by_id(champ_id: str, settings: _settings.Settings) -> _champion.Champion:
    """Retrieve champion object from champion id

    Args:
        champ_id (str): the numeric id of the champion
        settings (Settings): a setting object used to retrieve data_paths 

    Returns:
        Champion: a Champion object with all champion informations
    """
    # if not champ_id.isdigit():
    #     raise ValueError("champ_id must be digit")
    assert champ_id.isdigit(), ValueError("champ_id must be digit")
    champ_id = str(champ_id)
    full_data = get_champion_file(settings)
    try:
        champ_name = full_data["keys"][champ_id]
    except KeyError as err:
        raise _err.MissingChampId(champ_id) from err
    champ_data = get_champion_by_name(champ_name=champ_name, settings=settings)
    return champ_data


def check_url(api_url: str) -> str:
    """ checks if passed in urls are relative or absolute """
    if api_url.startswith("http"):
        return api_url
    return ""
