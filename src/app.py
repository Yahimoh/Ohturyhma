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
    return render_template("index.html", viitteet=lue_viitteet())

@app.route("/send", methods=["POST"])
def send():
    viite = Viite({
        "nimi": request.form["viite"],
        "kirjailija": request.form["kirjailija"],
        "otsikko": request.form["otsikko"],
        "vuosi": int(request.form["vuosi"]),
        "kustantaja": request.form["kustantaja"],
    })

    lisaa_viite(viite)

    return redirect("/")
