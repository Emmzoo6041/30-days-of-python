import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def print_weather_info(weather_data):
    if weather_data.get('cod') != 200:
        print(f"Error: {weather_data.get('message')}")
        return

    main = weather_data['main']
    wind = weather_data['wind']
    weather = weather_data['weather'][0]

    print(f"City: {weather_data['name']}")
    print(f"Temperature: {main['temp']}°C")
    print(f"Humidity: {main['humidity']}%")
    print(f"Pressure: {main['pressure']} hPa")
    print(f"Weather: {weather['description']}")
    print(f"Wind Speed: {wind['speed']} m/s")
    print(f"Wind Direction: {wind['deg']}°")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    city_name = input("Enter city name: ")
    weather_data = get_weather(city_name, api_key)
    print_weather_info(weather_data)

