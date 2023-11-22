from flask import Flask
from flask import redirect, render_template, request

app = Flask(__name__)

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
