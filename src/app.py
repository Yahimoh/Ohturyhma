from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///user"
db = SQLAlchemy(app)

@app.route("/")
def order():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    kirjailija = request.form["kirjailija"]
    otsikko = request.form["otsikko"]
    vuosi = request.form["vuosi"]
    kustantaja = request.form["kustantaja"]

    return redirect("/")
