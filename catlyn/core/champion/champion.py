"""Contains the Champion class representing a single champion instance"""


class Champion():
    """Representing a single champion object"""

    def __init__(self, champ_data: dict) -> None:
        self.spells = list()
        self.tags = list()
        self.name = str()
        self.title = str()
        self.stats = dict()
        self.key = int()
        self.__load_data(champ_data)

    # * PRIVATE AND PROTECTED METHODS

    def __load_data(self, champ_data: dict) -> None:
        """Loads all data from the passed in dict into class attributes"""
        if not isinstance(champ_data, dict):
            raise TypeError(f"Cannot initialize Champion object with argument of type {type(champ_data)}")
        self.tags = champ_data["tags"]
        self.name = champ_data["id"]
        self.key = int(champ_data["key"])
        self.title = champ_data["title"]
        self.stats = champ_data["stats"]
        self.__load_spells(champ_data["spells"])

    def __load_spells(self, spells: list) -> None:
        lookup_spells = {0: "Q", 1: "W", 2: "E", 3: "R"}
        for i, spell in enumerate(spells):
            spell_data = {
                "key": lookup_spells[i],
                "name": spell["name"],
                "description": spell["description"],
                "costBurn": spell["costBurn"],
                "costType": spell["costType"]
            }
            self.spells.append(spell_data)

    # * PUBLIC METHODS

    @property
    def json(self) -> dict:
        """Returns a json serializable dict"""
        data = {
            "key": self.key,
            "name": self.name,
            "title": self.title,
            "stats": self.stats,
            "spells": self.spells
        }
        return data
