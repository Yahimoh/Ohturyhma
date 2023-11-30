
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

        print(self.tiedot)
        viite = "@" + self.tiedot["tyyppi"] + "{" + self.tiedot["viite"] + ",\n"

        for avain, arvo in self.tiedot.items():
            if avain != "tyyppi" and avain != "viite" and avain != "id" and arvo != None:
                viite += f"    {avain} = {{{arvo}}},\n"

        viite += "}\n"
        return viite
