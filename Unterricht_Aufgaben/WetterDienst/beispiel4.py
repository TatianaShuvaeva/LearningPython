from flask import Flask
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
    
    wetter= wetter_dienst.get("Potsdam")
    return wetter


app.run(host='0.0.0.0', port=5000)()
