import requests

URL = "https://api.pokemonbattle.me:9104"
HEADER = {"Content-Type" : "application/json", "trainer_token" : "5c6b40f4c4f21bd94808f89a303cc416"}

body_post = {
      "name": "Бульба",
      "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_put = {
    "pokemon_id": "28758",
    "name": "New Name"
    }
body_in_pokeball = {
    "pokemon_id": "28758",
    }

response = requests.post (url= f'{URL}/pokemons', headers=HEADER,json=body_post,timeout=5)
print(f'Статус код: {response.status_code}. Сообщение:{response.json()["message"]}') 

response = requests.put(url= f'{URL}/pokemons', headers=HEADER,json=body_put,timeout=5)
print(f'Сообщение:{response.json()["message"]}') 

response = requests.put(url= f'{URL}/trainers/add_pokeball', headers=HEADER,json=body_in_pokeball,timeout=5)
print(f'Сообщение:{response.json()["message"]}')