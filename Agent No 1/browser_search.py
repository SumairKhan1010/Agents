import requests

def get_weather(lat: float, long: float) -> dict:
    """
    Get current weather for a location
    Args: 
    lat: latitude like 32.1
    long: longitude like 69.8 
    """

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
            "latitude": lat, 
            "longitude": long, 
            "current": "temperature_2m,wind_speed_10m"
        }

    response = requests.get(url, params=params)
    data = response.json()

    return data

def get_country(country: str) ->dict:

    """Get Country Info
    Args:
     country: country name like pakistan"""

    url = "https://restcountries.com/v3.1/all"

    params= {
            "fields": "name, capital,population, flags"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data

def get_books_info(topic: str) -> dict:

    """
    Get books info about topic
    Args: 
        topic: book info you want for specified topic
    """

    url = "https://openlibrary.org/search.json"

    params = {
        "q": topic, 
        "fields": "title,auther_name, first_publish_year,edition_count,cover_i",
        "limit": 5
    }

    response = requests.get(url, params=params)
    data = response.json()

    l = []

    for book in data["docs"]:
        l.append(book)

    return l
