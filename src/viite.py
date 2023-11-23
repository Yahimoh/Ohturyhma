
class Viite:
    """Luokka yhdelle viitteelle. 
    """
    def __init__(self, tiedot: dict):
        """Alustuksen yhteydessä anna
        viittauksen tiedot.

        Args:
            tiedot (dict): sanakirja muotoa {"nimi": "esimerkki"}
        """
        self.tiedot = tiedot

    def __str__(self) -> str:
        """Esittää viitteen tiedot bibtex-muodossa.
        Automaattisesti rakentaa oikeanlaisen muodon
        sanakirjan perusteella.
        """
        # Yahia muuta tämä siten, että oikean näköinen bibtex-muoto
        viite = f"""@book{{{self.tiedot["viite"]}, <br>
&emsp; title = "{self.tiedot["otsikko"]}"<br>
 &emsp;   author = "{self.tiedot["kirjailija"]}"<br>
 &emsp;   year = "{self.tiedot["vuosi"]}"<br>
 &emsp;   publisher = "{self.tiedot["kustantaja"]}"<br>
}}<br>
"""
        return viite

class ViiteLista:
    """Luokka hallinnoimaan viitteitä. 
    Pääohjelma kutsuu tätä luokkaa viitteiden
    esittämisessä.
    """
    def __init__(self):
        self.viitteet = []
    
    def lisaa_viite(self, viite: Viite):
        """Lisää viite viitelistaan.
        """
        self.viitteet.append(viite)

    def hae_viitelista(self):
        """Palauttaa listan, missä
        kirjaviitteet on esitetty 
        bibtex-muodossa merkkijonona.
        """
        return [viite.__str__() for viite in self.viitteet]



# esimerkki käytöstä
if __name__ == "__main__":
    viitteeni = ViiteLista()

    tietoa = {"nimi": "joonajoona", "julkaisuvuosi": "2000", "lempiväri": "punainen"}

    viitteeni.lisaa_viite(Viite(tiedot=tietoa))

    for i in viitteeni.hae_viitelista():
        print(i)
