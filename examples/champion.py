"""Contains an example of how the Champion class should be instanced and a few use of it"""
import json
from catlyn import Catlyn, Settings

CONFIGS = "example_config.json"
SECRETS = "../catlyn/config/secrets.json"

SETTINGS = Settings(CONFIGS, SECRETS)
catlyn = Catlyn(settings=SETTINGS)

# EXAMPLE 1
data = catlyn.get_champion_by_id(champ_id="888")
print(json.dumps(data, indent=4, ensure_ascii=False))
