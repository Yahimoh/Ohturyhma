from flask import Flask
from flask import redirect, render_template, request
from src.database import lisaa_viite, db, lue_viitteet, poista_kaikki_viitteet, poista_viite, poista_viite_tyyppi, muokkaa_kirjaviitetta, muokkaa_artikkeliviitetta, hae_viite
from src.viite import Viite, maarita_nimi
from src.config import DATABASE_URL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db.init_app(app)

@app.route("/")
def order():
    return render_template("index.html",
                viitteet=[(x, str(x)) for x in lue_viitteet()], muokattava=False)

@app.route("/filter/<tyyppi>")
def filter_viitteet(tyyppi):
    return render_template("index.html",
                viitteet=[(x, str(x)) for x in lue_viitteet(tyyppi=tyyppi)], muokattava=False)

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

@app.route('/muokkaa_kirjaviite/<int:id>', methods=['POST'])
def muokkaa(id):
    kirjailija = request.form['kirjailija']
    otsikko = request.form['otsikko']
    vuosi = request.form['vuosi']
    kustantaja = request.form['kustantaja']
    tiedot = {"kirjailija":kirjailija, "otsikko":otsikko, "vuosi":vuosi, "kustantaja":kustantaja}

    muokkaa_kirjaviitetta(id, tiedot)
    return redirect('/')

@app.route('/muokkaa_artikkeliviitetta/<int:id>', methods=['POST'])
def muokkaa_artikkeli(id):
    kirjailija = request.form['kirjailija']
    otsikko = request.form['otsikko']
    vuosi = request.form['vuosi']
    kustantaja = request.form['kustantaja']
    sivut = request.form['sivut']
    julkaisunumero = request.form['julkaisunumero']
    tiedot = {"kirjailija":kirjailija, "otsikko":otsikko, "vuosi":vuosi, "kustantaja":kustantaja, "julkaisunumero":julkaisunumero, "sivut":sivut}
    
    muokkaa_artikkeliviitetta(id, tiedot)
    return redirect('/')

@app.route("/lataa_viitteen_tiedot/<int:id>", methods=['POST'])
def lataa_viitteen_tiedot(id):
    viite = hae_viite(id)
    
    return render_template("index.html", muokattava=viite, viitteet=[(x, str(x)) for x in lue_viitteet()])




