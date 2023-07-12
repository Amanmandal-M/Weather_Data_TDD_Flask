<h1 align="center">Weather Backend API</h1>

This project implements a simple Flask-based backend API for weather data. It allows users to retrieve weather information for specific cities, add new weather data, update existing weather data, and delete weather data for a city.

## Project Structure

The project follows the following folder structure:

- `app.py`: The main Flask application file. It initializes the Flask app, registers routes, and starts the server.
- `routes/weather_routes.py`: Defines the routes for weather data operations.
- `controllers/weather_controllers.py`: Contains the controller functions for handling weather data operations.
- `tests/weather_test.py`: Contains test cases to verify the functionality of the API endpoints.

## Usage

1. Start the server by running the `app.py` file.
2. Access the API endpoints using the following routes:

   - `GET /weather-api/weather/<city>`: Retrieve weather data for a specific city.
   - `POST /weather-api/weather`: Add new weather data for a city.
   - `PUT /weather-api/weather/<city>`: Update weather data for a specific city.
   - `DELETE /weather-api/weather/<city>`: Delete weather data for a specific city.

   Replace `<city>` with the name of the city you want to perform the operation on.

## API Documentation

### Retrieve Weather Data

- **Endpoint**: `GET /weather-api/weather/<city>`
- **Description**: Retrieve weather data for a specific city.
- **Response**: JSON object containing the weather information for the city.

### Add Weather Data

- **Endpoint**: `POST /weather-api/weather`
- **Description**: Add new weather data for a city.
- **Request Body**: JSON object containing the city, temperature, and weather information.
- **Response**: JSON object containing the success message and the added weather data.

### Update Weather Data

- **Endpoint**: `PUT /weather-api/weather/<city>`
- **Description**: Update weather data for a specific city.
- **Request Body**: JSON object containing the updated temperature and/or weather information.
- **Response**: JSON object containing the updated weather data.

### Delete Weather Data

- **Endpoint**: `DELETE /weather-api/weather/<city>`
- **Description**: Delete weather data for a specific city.
- **Response**: JSON object confirming the deletion of the weather data.

## Testing

The project includes test cases to verify the functionality of the API endpoints. The test cases are defined in the `tests/weather_test.py` file.

To run the tests, use the following command:

```shell
pytest tests/weather_test.py
```

Note : Make sure you have the `pytest` library installed.