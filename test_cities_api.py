#!/usr/bin/python3

import requests
import json

BASE_URL = 'http://0.0.0.0:5000/api/v1'

def test_get_cities_by_state():
    state_id = '421a55f4-7d82-47d9-b54c-a76916479548'
    url = '{}/states/{}/cities'.format(BASE_URL, state_id)
    response = requests.get(url)
    assert response.status_code == 200
    cities = response.json()
    assert isinstance(cities, list)
    assert all('name' in city for city in cities)

def test_get_city_by_id():
    city_id = '521a55f4-7d82-47d9-b54c-a76916479548'
    url = '{}/cities/{}'.format(BASE_URL, city_id)
    response = requests.get(url)
    assert response.status_code == 200
    city = response.json()
    assert 'name' in city

def test_create_city():
    state_id = '421a55f4-7d82-47d9-b54c-a76916479548'
    url = '{}/states/{}/cities'.format(BASE_URL, state_id)
    data = {'name': 'Test City'}
    response = requests.post(url, json=data)
    assert response.status_code == 201
    city = response.json()
    assert 'name' in city and city['name'] == 'Test City'

def test_update_city():
    city_id = '521a55f4-7d82-47d9-b54c-a76916479548'
    url = '{}/cities/{}'.format(BASE_URL, city_id)
    data = {'name': 'Updated City Name'}
    response = requests.put(url, json=data)
    assert response.status_code == 200
    updated_city = response.json()
    assert updated_city['name'] == 'Updated City Name'

def test_delete_city():
    city_id = '521a55f4-7d82-47d9-b54c-a76916479548'
    url = '{}/cities/{}'.format(BASE_URL, city_id)
    response = requests.delete(url)
    assert response.status_code == 200
    assert response.json() == {}

def test_invalid_json():
    state_id = '421a55f4-7d82-47d9-b54c-a76916479548'
    url = '{}/states/{}/cities'.format(BASE_URL, state_id)
    data = '{"invalid": "json"}'
    response = requests.post(url, data=data)
    assert response.status_code == 400
    assert response.json()['error'] == 'Not a JSON'

def test_non_existing_city():
    city_id = 'non_existing_city_id'
    url = '{}/cities/{}'.format(BASE_URL, city_id)
    response = requests.get(url)
    assert response.status_code == 404
    assert response.json()['error'] == 'Not found'

if __name__ == '__main__':
    test_get_cities_by_state()
    test_get_city_by_id()
    test_create_city()
    test_update_city()
    test_delete_city()
    test_invalid_json()
    test_non_existing_city()

    print("All tests passed!")
