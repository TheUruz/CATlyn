"""This module contains the ChampionList class which is used to represents lists of Champion objects"""
from catlyn.core.champion.champion import Champion


class ChampionsList():
    """ Class that handles collections of champions """

    def __init__(self, champions_list: list[Champion]) -> None:
        self.__champions_list = champions_list
