
class Viite:
    """Luokka yhdelle viitteelle. 
    """
    def __init__(self, tiedot):
        """Alustuksen yhteydessä anna
        viittauksen tiedot.
        Viitteen tyyppi ja nimi tulee antaa argumenttina.

        Args:
            tiedot (dict): sanakirja muotoa {"nimi": "esimerkki"}
        """
        self.tiedot = tiedot
        #self.id = self.tiedot.get("id", None)

    def __str__(self) -> str:
        """Esittää viitteen tiedot bibtex-muodossa.
        Automaattisesti rakentaa oikeanlaisen muodon
        sanakirjan perusteella.
        """
        #nimi = self.tiedot["viite"]
        #viitetyyppi = self.tiedot["tyyppi"]

        viite = "@" + "nimi" + "{" + "nimi" + ",<br>"

        for avain, arvo in self.tiedot.items():
            viite += f"{avain:12}   =   {{{arvo}}},<br>"

        #viite = viite[:-2] + viite[-1:]
        viite += "}<br>"
        return viite
