DROP TABLE IF EXISTS KirjaViitteet;
CREATE TABLE KirjaViitteet (id SERIAL PRIMARY KEY, viite TEXT, vuosi INTEGER, kirjailija TEXT, otsikko TEXT, kustantaja TEXT, versio INTEGER);