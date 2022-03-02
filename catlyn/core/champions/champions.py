from typing import List
from catlyn.core.champion.champion import Champion


class ChampionsList():
    """ Class that handles collections of champions """

    def __init__(self, champions_list: List[Champion]) -> None:
        self.__champions_list = champions_list
