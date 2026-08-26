import requests

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

# WMO weather codes -> human readable text
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}

COMPASS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
           "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

def describe(code: int) -> str:
    return WEATHER_CODES.get(code, f"Unknown (code {code})")

def to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

def to_mph(kmh: float) -> float:
    return kmh * 0.621371

def to_compass(degrees: float) -> str:
    """Turn a wind bearing in degrees into a compass point like 'SE'."""
    return COMPASS[round(degrees / 22.5) % 16]

def find_city(city: str):
    """Turn a city name into coordinates using the geocoding API."""
    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json",
    }
    response = requests.get(GEOCODE_URL, params=params, timeout=10)
    response.raise_for_status()  # raise an error if the request failed

    results = response.json().get("results")
    if not results:
        raise ValueError(f"No location found for {city!r}")

    place = results[0]
    return {
        "name": place["name"],
        "country": place.get("country", ""),
        "latitude": place["latitude"],
        "longitude": place["longitude"],
    }

def get_weather(city: str, days: int = 3):
    """Fetch the current conditions plus a short daily forecast for a city."""
    place = find_city(city)

    params = {
        "latitude": place["latitude"],
        "longitude": place["longitude"],
        "current": ("temperature_2m,apparent_temperature,relative_humidity_2m,"
                    "wind_speed_10m,wind_direction_10m,cloud_cover,weather_code"),
        "daily": ("temperature_2m_max,temperature_2m_min,precipitation_sum,"
                  "precipitation_probability_max,weather_code"),
        "temperature_unit": "celsius",
        "wind_speed_unit": "kmh",
        "timezone": "auto",  # timestamps come back in the city's local time
        "forecast_days": days,
    }
    response = requests.get(FORECAST_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    current = data["current"]
    daily = data["daily"]

    forecast = []
    for i, date in enumerate(daily["time"]):
        forecast.append({
            "date": date,
            "high": daily["temperature_2m_max"][i],
            "low": daily["temperature_2m_min"][i],
            "precipitation": daily["precipitation_sum"][i],
            "rain_chance": daily["precipitation_probability_max"][i],
            "conditions": describe(daily["weather_code"][i]),
        })

    return {
        "place": place,
        "current": {
            "time": current["time"],  # local observation time, not when you ran this
            "temperature": current["temperature_2m"],
            "feels_like": current["apparent_temperature"],
            "humidity": current["relative_humidity_2m"],
            "wind_speed": current["wind_speed_10m"],
            "wind_direction": current["wind_direction_10m"],
            "cloud_cover": current["cloud_cover"],
            "conditions": describe(current["weather_code"]),
        },
        "forecast": forecast,
    }

if __name__ == "__main__":
    report = get_weather("Ames", days=3)

    place = report["place"]
    current = report["current"]
    print(f"\nWeather for {place['name']}, {place['country']} "
          f"({place['latitude']:.2f}, {place['longitude']:.2f})")
    print(f"As of: {current['time']} local time")

    temp_c = current["temperature"]
    feels_c = current["feels_like"]
    print(f"Now: {temp_c} C / {to_fahrenheit(temp_c):.0f} F, {current['conditions']} "
          f"(feels like {feels_c} C / {to_fahrenheit(feels_c):.0f} F)")
    print(f"Cloud cover: {current['cloud_cover']}%   Humidity: {current['humidity']}%")
    print(f"Wind: {to_mph(current['wind_speed']):.0f} mph from the "
          f"{to_compass(current['wind_direction'])}")

    print("\nForecast:")
    for day in report["forecast"]:
        print(f"  {day['date']}: {day['low']}-{day['high']} C "
              f"({to_fahrenheit(day['low']):.0f}-{to_fahrenheit(day['high']):.0f} F), "
              f"{day['conditions']}, {day['rain_chance']}% chance, "
              f"{day['precipitation']} mm")
