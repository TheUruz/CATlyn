import json
from typing import Any
from catlyn.core.utils import Settings


class Champion():
    """Representing a champion object """

    def __init__(self, champ_id: int, champ_name: str) -> None:
        self.__champ_id = champ_id
        self.__champ_name = champ_name


def get_champion_file(settings: Settings) -> dict:
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


def get_champion_by_name(champ_name: str, settings: Settings) -> Any:
    """Retrieve champion object from a champion name

    Args:
        champ_name (str): the name of the champion (case sensitive)
        settings (Settings): a setting object used to retrieve data_paths 

    Returns:
        Champion: a Champion object with all champion informations
    """
    full_data = get_champion_file(settings)
    champ_data = full_data["data"][champ_name]
    return champ_data


def get_champion_by_id(champ_id: str, settings: Settings) -> Champion:
    """Retrieve champion object from champion id

    Args:
        champ_id (str): the numeric id of the champion
        settings (Settings): a setting object used to retrieve data_paths 

    Returns:
        Champion: a Champion object with all champion informations
    """
    if not champ_id.isdigit():
        raise ValueError("champ_id must be digit")
    champ_id = str(champ_id)
    full_data = get_champion_file(settings)
    champ_name = full_data["keys"][champ_id]
    champ_data = get_champion_by_name(champ_name=champ_name, settings=settings)
    return champ_data
