#!/usr/bin/env python3


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


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
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
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


def get_location(city):
    """Convert a city name into latitude/longitude."""
    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json",
    }

    response = requests.get(GEOCODING_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if not data.get("results"):
        raise ValueError(f"Could not find city: {city}")

    result = data["results"][0]

    return {
        "name": result["name"],
        "country": result.get("country", ""),
        "latitude": result["latitude"],
        "longitude": result["longitude"],
    }


def get_weather(latitude, longitude, fahrenheit=False):
    """Fetch current weather and a 7-day forecast."""

    temperature_unit = "fahrenheit" if fahrenheit else "celsius"
    wind_speed_unit = "mph" if fahrenheit else "kmh"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "apparent_temperature,"
            "weather_code,"
            "wind_speed_10m"
        ),
        "daily": (
            "weather_code,"
            "temperature_2m_max,"
            "temperature_2m_min,"
            "precipitation_probability_max"
        ),
        "temperature_unit": temperature_unit,
        "wind_speed_unit": wind_speed_unit,
        "timezone": "auto",
        "forecast_days": 7,
    }

    response = requests.get(WEATHER_URL, params=params, timeout=10)
    response.raise_for_status()

    return response.json()


def print_current_weather(location, weather, fahrenheit=False):
    """Display current weather."""

    current = weather["current"]

    unit = "°F" if fahrenheit else "°C"
    wind_unit = "mph" if fahrenheit else "km/h"

    weather_description = WEATHER_CODES.get(
        current["weather_code"],
        "Unknown"
    )

    print()
    print("=" * 50)
    print(f"  WEATHER FOR {location['name'].upper()}, {location['country'].upper()}")
    print("=" * 50)

    print(f"  Condition:       {weather_description}")
    print(f"  Temperature:     {current['temperature_2m']:.1f}{unit}")
    print(f"  Feels like:      {current['apparent_temperature']:.1f}{unit}")
    print(f"  Humidity:        {current['relative_humidity_2m']}%")
    print(f"  Wind speed:      {current['wind_speed_10m']:.1f} {wind_unit}")

    print("=" * 50)


def print_forecast(weather, fahrenheit=False):
    """Display the 7-day forecast."""

    daily = weather["daily"]
    unit = "°F" if fahrenheit else "°C"

    print()
    print("7-DAY FORECAST")
    print("-" * 75)

    print(
        f"{'Date':<15}"
        f"{'Condition':<25}"
        f"{'Min':>10}"
        f"{'Max':>10}"
        f"{'Rain':>10}"
    )

    print("-" * 75)

    for i, date in enumerate(daily["time"]):
        condition = WEATHER_CODES.get(
            daily["weather_code"][i],
            "Unknown"
        )

        min_temp = daily["temperature_2m_min"][i]
        max_temp = daily["temperature_2m_max"][i]
        rain_probability = daily["precipitation_probability_max"][i]

        formatted_date = datetime.strptime(
            date, "%Y-%m-%d"
        ).strftime("%a %d %b")

        print(
            f"{formatted_date:<15}"
            f"{condition:<25}"
            f"{min_temp:>7.1f}{unit}"
            f"{max_temp:>7.1f}{unit}"
            f"{rain_probability:>7}%"
        )

    print("-" * 75)


def main():
    parser = argparse.ArgumentParser(
        description="Command-line weather application"
    )

    parser.add_argument(
        "city",
        nargs="+",
        help="City name, for example: London"
    )

    parser.add_argument(
        "--fahrenheit",
        "-f",
        action="store_true",
        help="Display temperatures in Fahrenheit"
    )

    args = parser.parse_args()

    city = " ".join(args.city)

    try:
        print(f"\nFetching weather for {city}...")

        location = get_location(city)

        weather = get_weather(
            location["latitude"],
            location["longitude"],
            args.fahrenheit
        )

        print_current_weather(
            location,
            weather,
            args.fahrenheit
        )

        print_forecast(
            weather,
            args.fahrenheit
        )

    except requests.exceptions.RequestException as error:
        print(f"\nNetwork error: {error}")
        sys.exit(1)

    except ValueError as error:
        print(f"\nError: {error}")
        sys.exit(1)

    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)


if __name__ == "__main__":
    main()
