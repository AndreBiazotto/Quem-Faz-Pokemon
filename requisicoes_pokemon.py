# Source - https://stackoverflow.com/a
# Posted by CrisPlusPlus
# Retrieved 2026-01-03, License - CC BY-SA 4.0

import requests

url = "https://pokeapi.co/api/v2/type/"
poke_request = requests.get(url)
types = poke_request.json()

pokemon = {}
for typ in types["results"]:    
    pokemon[typ["name"]] = {"Dano duplo a": [], "Dano metade a": [], "Sem dano a": []}
    type_request = requests.get(typ["url"])
    type_data = type_request.json()
    for double_damage_to in type_data["damage_relations"]["double_damage_to"]:
        pokemon[typ["name"]]["Dano duplo a"].append(double_damage_to["name"])
    for half_damage_to in type_data["damage_relations"]["half_damage_to"]:
        pokemon[typ["name"]]["Dano metade a"].append(half_damage_to["name"])
    for no_damage_to in type_data["damage_relations"]["no_damage_to"]:
        pokemon[typ["name"]]["Sem dano a"].append(no_damage_to["name"])
# print(pokemon)