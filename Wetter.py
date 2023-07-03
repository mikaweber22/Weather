# package namems "requests" importieren
import requests


# Funktion, die uns die Koordinaten für Stadt, Land zurückgibt.
def get_coordinates(city, country):
    base_url = "https://geocode.maps.co/search"
    params = {"q": f"{city}, {country}"}

    response = requests.get(base_url, params)
    coordinates = response.json()
    latitude = coordinates[0]["lat"]
    longitude = coordinates[0]["lon"]

    return latitude, longitude


# Funktion, die uns das Wetter für eine Stadt zurückgibt
def get_weather(city, country):
    # diese URL nutzen wir, um von dort die Wetterdaten zu kriegen
    base_url = "https://api.open-meteo.com/v1/forecast"

    # Koordinaten holen
    latitude, longitude = get_coordinates(city, country)

    # Dictionary ("Wörterbuch"): key-value-Struktur ("Name-Wert-Struktur")
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
    }

    # Anfrage an die Wetter-Schnittstelle
    response = requests.get(base_url, params)
    weather_data = response.json()
    current_weather = weather_data["current_weather"]

    weather = {
        "city": city,
        "country": country,
        "temperature": current_weather["temperature"],
        "windspeed": current_weather["windspeed"],
    }

    return weather


# Gibt das Wetter ordentlich lesbar aus
def print_weather(weather):
    city = weather["city"]  # "Hannover"
    country = weather["country"]  # "Rom"
    windspeed = weather["windspeed"]  # "2200000000000km/h"
    temperature = weather["temperature"]  # "20098483093°C."

    output = f"In {city}, {country} sind derzeit {temperature}°C."

    print(output)


print("Willkommen zur Wetter-App!\n")
while True:
    # definiere Variablen city und country
    city = input("\nStadt?\n")
    country = input("\nLand?\n")

    weather = get_weather(city, country)
    print_weather(weather)
