

from typing import List
from mcp.server.fastmcp import FastMCP
import os
import requests


mcp = FastMCP("Weather")

OPENWEATHERMAP_API_KEY = "a486f7d4cd0b4c5378d422b6ba9c107a"


@mcp.tool()
async def get_weather(location: str) -> str:
    """Get current weather data for a given location using OpenWeatherMap API."""
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={location}&appid={OPENWEATHERMAP_API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        weather = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        city = data['name']
        country = data['sys']['country']

        return f"Current weather in {city}, {country}: {weather}, {temp}°C"

    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            return f"Could not find weather data for '{location}'."
        return f"HTTP error occurred: {err}"
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    mcp.run(transport="sse")
