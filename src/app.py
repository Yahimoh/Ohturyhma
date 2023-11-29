from os import getenv
from flask import Flask
from flask import redirect, render_template, request
from src.database import lisaa_viite, db, lue_viitteet
from src.viite import Viite

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URL")
db.init_app(app)

@app.route("/")
def order():
    return render_template("index.html", viitteet=[[x.tiedot['id'], str(x)] for x in lue_viitteet()])

@app.route("/send_kirja", methods=["POST"])
def send_kirja():
    viite = Viite({
        "viite": request.form["viite"],
        "kirjailija": request.form["kirjailija"],
        "otsikko": request.form["otsikko"],
        "vuosi": int(request.form["vuosi"]),
        "kustantaja": request.form["kustantaja"],
    })

    lisaa_viite(viite)

    return redirect("/")

@app.route("/send_artikkeli", methods=["POST"])
def send_artikkeli():
    viite = Viite({
        "viite": request.form["viite"],
        "kirjailija": request.form["kirjailija"],
        "otsikko": request.form["otsikko"],
        "vuosi": int(request.form["vuosi"]),        
        "julkaisunumero": (request.form["julkaisunumero"]),
        "kustantaja": (request.form["kustantaja"]),
        "sivut": (request.form["sivut"])
    })

    lisaa_viite(viite)

    return redirect("/")
