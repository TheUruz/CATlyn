"""Contains all possibile CATlyn errors"""
from typing import Union


class MissingChampId(Exception):
    """ Raised when no id correspond to a champion"""

    def __init__(self, champ_id: Union[int, str]) -> None:
        self.error_msg = f"Cannot find any champion with id {champ_id}"
        super().__init__(self.error_msg)


class MissingChampName(Exception):
    """ Raised when a name doesn't correspond to any champion"""

    def __init__(self, champ_name: str) -> None:
        self.error_msg = f"Cannot find any champion named '{champ_name}'"
        super().__init__(self.error_msg)


class RiotKeyExpired(Exception):
    """Raised when the provided API key is expired"""

    def __init__(self) -> None:
        self.error_msg = "The provided Riot API key is expired. please refresh your API key"
        super().__init__(self.error_msg)
