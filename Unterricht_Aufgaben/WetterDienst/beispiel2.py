import os
from dotenv import load_dotenv
from Unterricht_Aufgaben.WetterDienst.cl_WetterDienst import WetterDienst


load_dotenv()

OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
if OPENWEATHERMAP_API_KEY is None:
    raise Exception("OPENWEATHERMAP_API_KEY nicht gefunden")

wetter_dienst = WetterDienst(OPENWEATHERMAP_API_KEY)

wetter_stadt = wetter_dienst.get("Potsdam")
print(wetter_stadt.temperature)
# temperatur_stadt = wetter_dienst.get("Paris")
# print(temperatur_stadt)


# wetter_stadt = wetter_dienst.get("Potsdam")
# print(wetter_stadt)
