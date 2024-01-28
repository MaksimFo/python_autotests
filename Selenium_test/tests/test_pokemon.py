import requests
import pytest

URL = "https://api.pokemonbattle.me:9104"
HEADER = {"Content-Type" : "application/json", "trainer_token" : "5c6b40f4c4f21bd94808f89a303cc416"}

def test_get_trainers():
    response = requests.get (url= f'{URL}/trainers', headers=HEADER,params={'trainer_id': 3751},timeout=5)
    assert response.status_code == 200, 'Unexpected status code'

def test_name_trainers():
    response = requests.get (url= f'{URL}/trainers', headers=HEADER,params={'trainer_id': 3751},timeout=5)
    assert response.json()['trainer_name'] == "Максим", "Unexpected name"