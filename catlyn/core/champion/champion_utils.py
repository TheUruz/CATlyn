import json
from catlyn.core.utils.errors import MissingChampId, MissingChampName
from catlyn.core.utils.settings import Settings
from catlyn.core.champion.champion import Champion


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


def get_champion_by_name(champ_name: str, settings: Settings) -> Champion:
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
        raise MissingChampName(champ_name) from err
    return champ_data


def get_champion_by_id(champ_id: str, settings: Settings) -> Champion:
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
        raise MissingChampId(champ_id) from err
    champ_data = get_champion_by_name(champ_name=champ_name, settings=settings)
    return champ_data
