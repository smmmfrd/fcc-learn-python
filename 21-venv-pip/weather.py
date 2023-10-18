import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def get_current_weather():
    print("\n*** Get Current Weather Conditions ***\n")

    city = input("\nPlease enter a city name:\n")

    req_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=imperial"

    weather_data = requests.get(req_url).json()

    # pprint(weather_data)

    print(f'\nCurrent weather for {weather_data["name"]}')
    print(f'\nTemp is {weather_data["main"]["temp"]}')
    print(
        f'\nTemp feels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.\n'
    )


if __name__ == "__main__":
    get_current_weather()
