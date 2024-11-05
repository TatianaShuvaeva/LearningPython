from functools import cache
import requests
import json


class WetterDienst:
    def __init__(self, api_key: str):
        self._api_key = api_key
        # https://example.com/path/to/page?name=ferret&color=purple
        self._base_url = (
            "https://api.openweathermap.org/data/2.5/weather"
            "?appid={api_key}"
            "&q={stadt_name}"
            "&units=metric"
        )

    @cache
    def get_temperatur(self, stadt: str) -> float:

        complete_url = self._base_url.format(stadt_name=stadt, api_key=self._api_key)
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != 200:
            raise Exception(x)

        temperatur = x["main"]["temp"]
        return temperatur
