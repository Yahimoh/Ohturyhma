
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


    def __str__(self) -> str:
        """Esittää viitteen tiedot bibtex-muodossa.
        Automaattisesti rakentaa oikeanlaisen muodon
        sanakirjan perusteella.
        """

        print(self.tiedot)
        viite = "@" + self.tiedot["tyyppi"] + "{" + self.tiedot["viite"] + ",\n"

        for avain, arvo in self.tiedot.items():
            if avain != "tyyppi" and avain != "viite" and avain != "id" and arvo is not None:
                viite += f"    {avain} = {{{arvo}}},\n"

        viite += "}\n"
        return viite
    
    def get_type(self):
        return self.tiedot["tyyppi"]

def maarita_nimi(kirjailija, vuosi):
    kirjailija_string = kirjailija.replace(" and ", ", ")
    kirjailija_string = kirjailija_string.replace(" ja ", ", ")
    
    kirjailijat = [name.split()[-1] for name in kirjailija_string.split(", ")]
    
    identifier = ''.join([author[0] for author in kirjailijat])
    identifier += str(vuosi)[-2:]
            
    return identifier