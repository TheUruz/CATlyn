"""Contains the Champion class representing a single champion instance"""
import json


class Champion():
    """Representing a single champion object"""

    def __init__(self, champ_id: int, champ_name: str) -> None:
        self.__champ_id = champ_id
        self.__champ_name = champ_name
