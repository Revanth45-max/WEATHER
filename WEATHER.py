import requests

def get_weather(api_key, location):
    """
    Fetch current weather data for the specified location.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error fetching weather data: {err}")
    return None

def display_weather(data):
    """
    Display weather information: temperature, humidity, and conditions.
    """
    if not data or data.get("cod") != 200:
        print("Could not retrieve weather data. Please check the location and try again.")
        return

    city = data.get("name")
    country = data.get("sys", {}).get("country")
    temp = data.get("main", {}).get("temp")
    humidity = data.get("main", {}).get("humidity")
    weather_conditions = data.get("weather", [{}])[0].get("description")

    print(f"Weather for {city}, {country}")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {weather_conditions.capitalize()}")

def main():
    print("Welcome to the Command-line Weather App")
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    if not api_key:
        print("API key is required to fetch weather data.")
        return

    location = input("Enter a location (city or ZIP code): ").strip()
    if not location:
        print("Location cannot be empty.")
        return

    data = get_weather(api_key, location)
    display_weather(data)

if __name__ == "__main__":
    main()

