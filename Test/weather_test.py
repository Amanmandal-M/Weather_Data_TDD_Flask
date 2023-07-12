import json
import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_weather(client):
    response = client.get('/weather-api/weather/San Francisco')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data == {'temperature': 14, 'weather': 'Cloudy'}


def test_get_weather_invalid_city(client):
    response = client.get('/weather-api/weather/Invalid City')
    data = json.loads(response.data)
    assert response.status_code == 404
    assert data == {'message': 'City not found'}


def test_create_weather(client):
    data = {
        'city': 'Chicago',
        'temperature': 18,
        'weather': 'Windy'
    }
    response = client.post('/weather-api/weather', json=data)
    data = json.loads(response.data)
    assert response.status_code == 201
    assert data['message'] == 'Data Successfully Added'
    assert data['weather'] == {'temperature': 18, 'weather': 'Windy'}


def test_create_weather_missing_data(client):
    data = {
        'temperature': 25,
        'weather': 'Sunny'
    }
    response = client.post('/weather-api/weather', json=data)
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data == {'message': 'City not found'}


def test_update_weather(client):
    data = {
        'temperature': 30,
        'weather': 'Hot'
    }
    response = client.put('/weather-api/weather/Los Angeles', json=data)
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data == {'temperature': 30, 'weather': 'Hot'}


def test_update_weather_invalid_city(client):
    data = {
        'temperature': 25,
        'weather': 'Sunny'
    }
    response = client.put('/weather-api/weather/Invalid City', json=data)
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data == {'message': 'City not found'}


def test_delete_weather(client):
    response = client.delete('/weather-api/weather/Seattle')
    assert response.status_code == 200


def test_delete_weather_invalid_city(client):
    response = client.delete('/weather-api/weather/Invalid City')
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data == {'message': 'City not found'}
