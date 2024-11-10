from functools import cache
import requests
import json
from datetime import datetime
from typing import Tuple

from Unterricht_Aufgaben.WetterDienst.nicht_gefunden_fehler import NichtGefundenFehler
from Unterricht_Aufgaben.WetterDienst.wetter import Wetter



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
    def get(self,  stadt: str) -> Wetter:

        complete_url = self._base_url.format(stadt_name=stadt, api_key=self._api_key)
        
        response = requests.get(complete_url)
        
        if response.status_code == 404:
            raise NichtGefundenFehler(f"{stadt} ist nicht gefunden")
        
        antwort_json = response.json()
        if antwort_json["cod"] != 200:
            print(response.text)
            raise Exception(antwort_json)

        temperatur = antwort_json["main"]["temp"]
        min_temperature = antwort_json["main"]["temp_min"]
        max_temperature = antwort_json["main"]["temp_max"]
        wind = antwort_json["wind"]["speed"]
        luftfeuchtigkeit = antwort_json["main"]["humidity"]
        sonnenaufgang = datetime.fromtimestamp(antwort_json["sys"]["sunrise"])
        sonnenuntergang = datetime.fromtimestamp(antwort_json["sys"]["sunset"])
        stadt = antwort_json["name"]
        
        return Wetter(temperatur, min_temperature, max_temperature, wind, luftfeuchtigkeit, sonnenaufgang, sonnenuntergang, stadt)
