import requests

class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000/"
        #self.reset_application()
#!
#uus route pitää lisätä että voi reset sivuston: 
#@app.route("/tests/reset", methods=["POST"])
#def reset_tests():
    #user_repository.delete_all()
    #return "Reset"
#!
    #def reset_application(self):
        #requests.post(f"{self._base_url}/tests/reset")
        
    def lisaa_kirjaviite(self, viite, kirjailija, otsikko, vuosi, kustantaja):
        data = {
            "viite": viite,
            "kirjailija": kirjailija,
            "otsikko": otsikko,
            "vuosi": vuosi,
            "kustantaja": kustantaja
        }
        
        requests.post(f"{self._base_url}/send", data=data)

    def lisaa_artikkeliviite(self, viite, kirjailija, otsikko, vuosi, kustantaja, julkaisunumero, sivut):
        data = {
            "viite": viite,
            "kirjailija": kirjailija,
            "otsikko": otsikko,
            "vuosi": vuosi,
            "kustantaja": kustantaja,
            "julkaisunumero": julkaisunumero,
            "sivut": sivut
        }
        
        requests.post(f"{self._base_url}/send", data=data)