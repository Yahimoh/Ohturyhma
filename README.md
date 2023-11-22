# Ohturyhma

[Product backlog](https://helsinkifi-my.sharepoint.com/:x:/g/personal/otpe_ad_helsinki_fi/EZ52qyApLT5KhC2W8aO7UAoBViIUBE0OcVd7s9KNCpp-zg?e=4%3AQaeh74&fromShare=true&at=9)

[Sprint backlog](https://helsinkifi-my.sharepoint.com/:x:/g/personal/otpe_ad_helsinki_fi/EQPD5vKTcAJCqVxXUmrJUmQB8VH2PkiYl4GyYAWsyuskJA?e=4%3AqtdKDz&fromShare=true&at=9)


### Definition of done
- Ominaisuus on toteutettu ja testattu
- Se voidaan halutessa laittaa tuotantoon
- Koodi on katselmoitu

### Asennusohjeet
1. Asenna PostgreSQL esimerkiksi [tällä](https://www.postgresql.org/download/) ohjeella.
   
2. Kloonaa repositorio
```git clone git@github.com:Yahimoh/Ohturyhma.git```.

4. Lataa riippuvuudet
```poetry install ```.

5. Luo projektin juurihakemistoon tiedosto ```.env``` ja kopioi siihen ```.env.templates``` sisältö. Aseta ```DATABASE_URL``` arvo. Kokeile yhteyden muodostamista terminaalissa komennolla ```psql <url>```, jossa ```url = DATABASE_URL```.

6. Käynnistä sovellus
```flask run```.

