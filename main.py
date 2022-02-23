"""Entry point for my CATlyn test"""

import json
import lib

CONFIGS = "config_files/config.json"
SECRETS = "config_files/secrets.json"

CATlyn = lib.CATlyn()
CATlyn.load_config(CONFIGS, SECRETS)

# EXAMPLE
data = CATlyn.get_champion_info(champ_name="Thresh")
print(json.dumps(data, indent=4, ensure_ascii=False))
