import json
from catlyn import Settings, champion_utils

CONFIGS = "example_config.json"
SECRETS = "../catlyn/config_files/secrets.json"

SETTINGS = Settings(CONFIGS, SECRETS)

# EXAMPLE
data = champion_utils.get_champion_by_id(settings=SETTINGS, champ_id="888")
print(json.dumps(data, indent=4, ensure_ascii=False))
