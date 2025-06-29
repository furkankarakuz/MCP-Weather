import os
import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

app = FastMCP("Weather")


@app.tool()
def get_weather(city: str, lang: str) -> dict:
    """
    Returns the current weather information for the specified city.
    """
    if not API_KEY:
        return {"error": "OpenWeather API key not found."}

    params = {"q": city, "appid": API_KEY, "units": "metric", "lang": lang}

    try:
        response = requests.get(BASE_URL, params=params)

        if response.status_code != 200:
            return {"error": response.get("message", "Unknown error")}

        data = response.json()

        weather_info = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"]
        }

        return {"weather": weather_info}

    except Exception as e:
        return {"error": str(e)}
