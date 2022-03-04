"""A custom library to work around Riot API"""

from .catlyn import Catlyn

from .shared import utils, errors

from .core.champion.champion import Champion

from .config.settings import Settings


VERSION = "0.0.1"
print(">> CATlyn version: ", VERSION)
