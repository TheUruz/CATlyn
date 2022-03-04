"""Utility classes and functions"""
#! watch out for circular imports since this module is meant to be imported by many packages

import json
from catlyn.config import settings as _settings

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


def check_url(api_url: str) -> str:
    """ checks if passed in urls are relative or absolute """
    if api_url.startswith("http"):
        return api_url
    return ""
