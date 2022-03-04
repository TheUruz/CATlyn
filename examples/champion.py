"""Contains an example of how the Champion class should be instanced and a few use of it"""
import json
from catlyn.config import settings
from catlyn.shared import utils

CONFIGS = "example_config.json"
SECRETS = "../catlyn/config/secrets.json"

SETTINGS = settings.Settings(CONFIGS, SECRETS)

# EXAMPLE 1
data = utils.get_champion_by_id(settings=SETTINGS, champ_id="888")
print(json.dumps(data, indent=4, ensure_ascii=False))
