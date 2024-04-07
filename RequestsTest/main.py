import requests

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : 'bd68dbd0b2f8e89d9df4c46e0a84e030'}


body = {
    "name": "Софа",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)

print(response.text)




body_new_name = {
    "pokemon_id": "14022",
    "name": "Чарли",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

response_name = requests.put(f'{URL}/pokemons', headers = HEADERS, json = body_new_name)

print(response_name.text)




body_pokeball = {
    "pokemon_id": "14024"
}

response_pokeball = requests.post(f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_pokeball)

print(response_pokeball.text)





