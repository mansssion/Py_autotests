import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : 'bd68dbd0b2f8e89d9df4c46e0a84e030'}

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'level': 1})
    assert response.status_code == 200

def test_name():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': 1969})
    assert response.json()['data'][0]['trainer_name'] == 'Локи'
