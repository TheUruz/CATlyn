"""Contains an example of how the Champion class should be instanced and a few use of it"""
import json
from catlyn import Catlyn, Settings

CONFIGS = "example_config.json"
SECRETS = "../catlyn/config/secrets.json"

SETTINGS = Settings(CONFIGS, SECRETS)
catlyn = Catlyn(settings=SETTINGS)

# EXAMPLE 1 (get by id)
champ_by_id = catlyn.get_champion_by_id(champ_id="888")
#print(json.dumps(champ_by_id.json, indent=4, ensure_ascii=False))


# EXAMPLE 2 (get by name)
champ_by_name = catlyn.get_champion_by_name(champ_name="Garen")
#print(json.dumps(champ_by_name.json, indent=4, ensure_ascii=False))

# EXAMPLE 3 (get current week's free champion rotation)
free_rotation = catlyn.get_free_rotation()
#print(*(f"KEY: {champ[0]} - CHAMPION: {champ[1]}" for champ in free_rotation), sep="\n")
