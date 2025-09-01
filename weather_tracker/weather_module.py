# weather_module.py

class Weather:
    def __init__(self, city, temperature, condition, humidity, wind_speed, last_updated):
        """
        Initialize Weather object with data
        """
        self.city = city
        self.temperature = temperature
        self.condition = condition
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.last_updated = last_updated

    def __str__(self):
        """
        String representation of the weather info
        """
        return (f"{self.city}: Temp = {self.temperature}°C, "
                f"Condition = {self.condition}, "
                f"Humidity = {self.humidity}%, "
                f"Wind = {self.wind_speed} km/h, "
                f"Last Updated = {self.last_updated}")
