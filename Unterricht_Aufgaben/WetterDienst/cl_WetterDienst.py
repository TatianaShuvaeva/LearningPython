from functools import cache
import requests
import json


class WetterDienst:
    def __init__(self, api_key: str):
        self._api_key = api_key
        self._base_url = "https://api.openweathermap.org/data/2.5/weather?"

    @cache
    def get_temperatur(self, stadt: str) -> float:

        complete_url = self._base_url + "appid=" + self._api_key + "&q=" + stadt + "&units=metric"

        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != 200:
            raise Exception(x)

        temperatur = x["main"]["temp"]
        return temperatur
