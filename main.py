"""Entry point for my custom Riot API"""

import json
import lib

CONFIGS = "config_files/config.json"
SECRETS = "config_files/secrets.json"

Riot = lib.RiotLoLAPI()
Riot.load_config(CONFIGS, SECRETS)

# EXAMPLE
data = Riot.get_champion_info(champ_name="Thresh")
print(json.dumps(data, indent=4, ensure_ascii=False))
