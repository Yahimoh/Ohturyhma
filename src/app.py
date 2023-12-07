from flask import Flask
from flask import redirect, render_template, request
from src.database import lisaa_viite, db, lue_viitteet, poista_kaikki_viitteet, poista_viite, poista_viite_tyyppi
from src.viite import Viite, maarita_nimi
from src.config import DATABASE_URL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db.init_app(app)

@app.route("/")
def order():
    return render_template("index.html",
                viitteet=[(x, str(x)) for x in lue_viitteet()])

@app.route("/filter/<type>")
def filter(type):
    return render_template("index.html",
                viitteet=[(x, str(x)) for x in lue_viitteet() if x.tiedot["tyyppi"] == type])

@app.route("/send_kirja", methods=["POST"])
def send_kirja():
    viite = Viite({
        "tyyppi": "book",
        "kirjailija": request.form["kirjailija"],
        "otsikko": request.form["otsikko"],
        "vuosi": int(request.form["vuosi"]),
        "kustantaja": request.form["kustantaja"],
        "viite": maarita_nimi(request.form["kirjailija"], request.form["vuosi"])
    })

    lisaa_viite(viite)

    return redirect("/")

@app.route("/send_artikkeli", methods=["POST"])
def send_artikkeli():
    viite = Viite({
        "tyyppi": "article",
        "kirjailija": request.form["kirjailija"],
        "otsikko": request.form["otsikko"],
        "vuosi": int(request.form["vuosi"]),        
        "julkaisunumero": (request.form["julkaisunumero"]),
        "kustantaja": (request.form["kustantaja"]),
        "sivut": (request.form["sivut"]),
        "viite": maarita_nimi(request.form["kirjailija"], request.form["vuosi"])
    })

    lisaa_viite(viite)

    return redirect("/")

@app.route('/poista_viitteet', methods=['POST'])
def poista_viitteet():
    poista_kaikki_viitteet()
    return redirect('/')

@app.route('/poista_kirja_viitteet', methods=['POST'])
def poista_kirja_viitteet():
    poista_viite_tyyppi("book")
    return redirect('/')

@app.route('/poista_artikkeli_viitteet', methods=['POST'])
def poista_artikkeli_viitteet():
    poista_viite_tyyppi("article")
    return redirect('/')

@app.route('/poista/<int:viite_id>', methods=['POST'])
def poista(viite_id):
    poista_viite(viite_id)
    return redirect('/')