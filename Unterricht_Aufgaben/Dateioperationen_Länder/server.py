from dataclasses import dataclass
from flask import Flask, Response, jsonify
from datei_einlesen import get_länder as get_länder_aus_datei, get_länder_hauptstädte as get_länder_hauptstädt_datei


@dataclass
class Land:
    name_land: str
    haupstadt: str

app = Flask(__name__)

@app.route("/api/laender-hauptstaedte", methods=["GET"])
def get_laender_hauptstaedte()-> Response:
    länder_hauptstädte = get_länder_hauptstädt_datei()
    länder = []
    
    for land_hauptstadt_als_string in länder_hauptstädte:
        land_hauptstadt = land_hauptstadt_als_string.split(' ')
        land = Land(name_land=land_hauptstadt[0], haupstadt=land_hauptstadt[1])
        länder.append(land)
    
    ergebnis = jsonify(länder)
    return ergebnis


@app.route("/api/laender", methods=["GET"])
def get_länder()-> Response:
    länder = get_länder_aus_datei()
    ergebnis = jsonify(länder)
    return ergebnis

@app.route("/")
def get_index() -> str:
    return (
        "<!DOCTYPE html>"
        "<html>"
        "<body>"

        "<h1>My First Heading</h1>"

        "<p>My first paragraph.</p>"

        "</body>"
        "</html>"
        
    )

app.run(debug=True)
