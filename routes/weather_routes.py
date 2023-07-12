from flask import Blueprint

# Import the required controllers
from controllers.weather_controllers import get_weather, create_weather, update_weather, delete_weather

# Create a Blueprint for the weather routes
weather_router = Blueprint('weather-api', __name__)

# Route to get weather data for a specific city
weather_router.route('/weather/<string:city>', methods=['GET'])(get_weather)

# Route to create new weather data for a city
weather_router.route('/weather', methods=['POST'])(create_weather)

# Route to update weather data for a specific city
weather_router.route('/weather/<string:city>', methods=['PUT'])(update_weather)

# Route to delete weather data for a specific city
weather_router.route('/weather/<string:city>', methods=['DELETE'])(delete_weather)
