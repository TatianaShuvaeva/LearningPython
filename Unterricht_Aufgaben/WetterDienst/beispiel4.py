from flask import Flask, Response, request
import os
from dotenv import load_dotenv
from Unterricht_Aufgaben.WetterDienst.cl_WetterDienst import WetterDienst
from Unterricht_Aufgaben.WetterDienst.nicht_gefunden_fehler import NichtGefundenFehler


load_dotenv()

OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
if OPENWEATHERMAP_API_KEY is None:
    raise Exception("OPENWEATHERMAP_API_KEY nicht gefunden")

app = Flask('WetterDienst')

wetter_dienst = WetterDienst(OPENWEATHERMAP_API_KEY)


@app.route('/')
def hello_world():

    current_directory = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    path_to_file = os.path.join(current_directory, 'index.html')

    with open(path_to_file, 'r') as file:
        file_content = file.read()
        return file_content


@app.route('/wetter')
def get_wetter():
    ausgewaehlte_stadt = request.args.get('stadt')
    if ausgewaehlte_stadt is None:
        return Response("Stadt ist None", status=400)

    try:
        wetter_stadt = wetter_dienst.get(ausgewaehlte_stadt)

    except NichtGefundenFehler as error:
        print(error)
        return Response(f"{ausgewaehlte_stadt} ist nicht gefunden", status=404)

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
