from flask import request, jsonify

# Dictionary to store weather data
weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}


def get_weather(city):
    # Check if the city exists in the weather_data dictionary
    if city not in weather_data:
        return jsonify({'message': 'City not found'}), 404

    # Retrieve the weather information for the city
    weather = weather_data[city]
    return jsonify(weather), 200


def create_weather():
    # Get the weather data from the request JSON
    weather = request.get_json()

    # Check if the required fields are present in the weather data
    if 'city' not in weather:
        return jsonify({'message': 'City not found'}), 400

    if 'temperature' not in weather:
        return jsonify({'message': 'Temperature not found'}), 400

    if 'weather' not in weather:
        return jsonify({'message': 'Weather not found'}), 400

    # Extract the data from the request JSON
    city = weather['city']
    temperature = weather['temperature']
    weather_condition = weather['weather']

    # Add the weather data to the weather_data dictionary
    weather_data[city] = {'temperature': temperature, 'weather': weather_condition}

    return jsonify({
        "message": "Data Successfully Added",
        "weather": weather_data[city]
    }), 201


def update_weather(city):
    # Check if the city exists in the weather_data dictionary
    if city not in weather_data:
        return jsonify({'message': 'City not found'}), 400

    # Get the weather data from the request JSON
    weather = request.get_json()

    # Update the temperature and weather condition if provided in the request JSON
    temperature = weather.get('temperature')
    weather_condition = weather.get('weather')

    if temperature is not None:
        weather_data[city]['temperature'] = temperature

    if weather_condition is not None:
        weather_data[city]['weather'] = weather_condition

    return jsonify(weather_data[city])


def delete_weather(city):
    # Check if the city exists in the weather_data dictionary
    if city not in weather_data:
        return jsonify({'message': 'City not found'}), 400

    # Delete the weather data for the city
    del weather_data[city]

    return jsonify({'message': f"{city} Deleted Successfully"})
