from flask import Flask
from flask import redirect, render_template, request
from src.database import db
from sqlalchemy.sql import text
from os import getenv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URL")
db.init_app(app)

@app.route("/")
def order():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    viite = request.form["viite"]
    kirjailija = request.form["kirjailija"]
    otsikko = request.form["otsikko"]
    vuosi = int(request.form["vuosi"])
    kustantaja = request.form["kustantaja"]

    sql = text("INSERT INTO KirjaViitteet (viite, kirjailija, otsikko, vuosi, kustantaja) VALUES (:viite, :kirjailija, :otsikko, :vuosi, :kustantaja);")
    db.session.execute(sql, {"viite": viite,
                             "kirjailija": kirjailija,
                             "otsikko": otsikko,
                             "vuosi": vuosi, 
                             "kustantaja": kustantaja})
    db.session.commit()

    return redirect("/")