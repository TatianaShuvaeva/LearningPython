from flask import Flask, Response, request
import os
from dotenv import load_dotenv
from Unterricht_Aufgaben.WetterDienst.cl_WetterDienst import WetterDienst


load_dotenv()

OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
if OPENWEATHERMAP_API_KEY is None:
    raise Exception("OPENWEATHERMAP_API_KEY nicht gefunden")

app = Flask('WetterDienst')

wetter_dienst = WetterDienst(OPENWEATHERMAP_API_KEY)


@app.route('/')
def hello_world():
    return 'Hello World! '


@app.route('/wetter')
def get_wetter():
    if request.args.get('stadt') is None:
        return Response("Stadt ist None", status=400)
    wetter_stadt = wetter_dienst.get(request.args.get('stadt'))

    return {
        'temperature': wetter_stadt.temperature,
        'min_temperature': wetter_stadt.min_temperature,
        'max_temperature': wetter_stadt.max_temperature,
        'wind': wetter_stadt.wind,
        'luftfeuchtigkeit': wetter_stadt.luftfeuchtigkeit,
        'sonnenaufgang': wetter_stadt.sonnenaufgang.isoformat(),
        'sonnenuntergang': wetter_stadt.sonnenuntergang.isoformat(),
        'stadt': wetter_stadt.stadt

    }


app.run(host='0.0.0.0', port=5000)()
