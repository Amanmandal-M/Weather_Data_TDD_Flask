import os
from flask import Flask
from flask_cors import CORS

# All routes imported
from routes.weather_routes import weather_router


app = Flask(__name__)

app.debug = True

# Enable CORS for all routes
CORS(app)

# Default routes
@app.route('/')
def default_routes():
    return '<h1 style="color:blue;text-align:center">Welcome to Weather Backend TDD!</h1>'

# Register the routes blueprint
app.register_blueprint(weather_router, url_prefix='/weather-api')


if __name__ == '__main__':
    port = os.environ.get("PORT") or 9090
    app.run(host='0.0.0.0', port=port)
