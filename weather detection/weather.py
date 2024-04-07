import requests

def get_weather(latitude, longitude, api_key):
    try:
        url = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&exclude=minutely&appid={api_key}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404, 500)
        data = response.json()

        if 'current' in data:
            weather_info = {
                'temperature': data['current']['temp'],
                'description': data['current']['weather'][0]['description']
            }
            return weather_info
        else:
            print("Error: Unexpected response format from the API.")
            return None
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def main():
    latitude = input("Enter latitude: ")
    longitude = input("Enter longitude: ")
    api_key = input("Enter your OpenWeatherMap API key: ")

    weather = get_weather(latitude, longitude, api_key)
    if weather:
        print("Current Weather:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
    else:
        print("Failed to fetch weather data. Please check your input and try again.")

if __name__ == "__main__":
    main()
