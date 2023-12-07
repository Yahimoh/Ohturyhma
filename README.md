![GHA workflow badge](https://github.com/Yahimoh/ohtuvarasto/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/Yahimoh/Ohturyhma/graph/badge.svg?token=J15WYOCCG8)](https://codecov.io/gh/Yahimoh/Ohturyhma)

# Ohturyhma

[Backlogit](https://helsinkifi-my.sharepoint.com/:x:/g/personal/otpe_ad_helsinki_fi/EQPD5vKTcAJCqVxXUmrJUmQB8VH2PkiYl4GyYAWsyuskJA?e=4%3AqtdKDz&fromShare=true&at=9)


### Definition of done
- Ominaisuus on toteutettu ja tarpeeksi testattu
- Ohjelma voidaan halutessa laittaa tuotantoon
- Koodi on katselmoitu

### Asennusohjeet
1. Asenna PostgreSQL esimerkiksi [tällä](https://www.postgresql.org/download/) ohjeella.
   
2. Kloonaa repositorio
```git clone git@github.com:Yahimoh/Ohturyhma.git```.

4. Lataa riippuvuudet
```poetry install ```. Jos asennusprosessi antaa virheilmoituksen paketin `psycopg2` kohdalla, testaa asentaa kirjasto `libpq-dev`. (Linux)

5. Luo postgresql-tietokanta nimellä `ohtu`.

6. Kopioi tiedoston `schema.sql` sisältö tietokantaan, esim. komennolla `psql ohtu < schema.sql`.

7. Luo projektin juurihakemistoon tiedosto ```.env``` ja kopioi siihen tiedoston ```.env.template``` sisältö. Aseta muuttujalle ```DATABASE_URL``` arvoksi luomasi tietokannan osoite. (esim. `postgresql:///ohtu`) Kokeile yhteyden muodostamista terminaalissa komennolla ```psql <url>```, jossa ```url = DATABASE_URL```.

8. Käynnistä sovellus komennolla 
```poetry run flask run```.

## Testaaminen

### Yksikkötestit
Ennen testaamista, luo uusi tietokanta. Tämän jälkeen luo `.env.test`-tiedosto juurihakemistoon ja kopioi siihen `.env.template`-tiedoston sisältö, mutta aseta `DATABASE_URL` uuden testitietokannan osoitteeksi.

Suorita testit komennolla
```poetry run pytest src```.
