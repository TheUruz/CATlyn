import json
import catlyn

CONFIGS = "example_config.json"
SECRETS = "../catlyn/config_files/secrets.json"

SETTINGS = catlyn.Settings(CONFIGS, SECRETS)

# EXAMPLE
data = catlyn.get_champion_by_id(settings=SETTINGS, champ_id="51")
print(json.dumps(data, indent=4, ensure_ascii=False))
