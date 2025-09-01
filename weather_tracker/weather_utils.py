# weather_utils.py

import requests
from weather_module import Weather

API_KEY = "b2f80fa27190445daa7151639250109"
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def fetch_weather(city):
    """
    Fetch weather data for a given city using WeatherAPI.com
    Returns a Weather object or None if error
    """
    try:
        url = f"{BASE_URL}?key={API_KEY}&q={city}"
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            print(f"Error: Could not fetch weather for {city}. (Status {response.status_code})")
            return None

        data = response.json()

        # Handle possible API error messages
        if "error" in data:
            print(f"API Error for {city}: {data['error']['message']}")
            return None

        # Extract relevant information
        city_name = data["location"]["name"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_kph"]
        last_updated = data["current"]["last_updated"]

        return Weather(city_name, temperature, condition, humidity, wind_speed, last_updated)

    except requests.exceptions.RequestException as e:
        print(f"Network error while fetching {city}: {e}")
        return None
