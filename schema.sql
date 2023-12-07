DROP TABLE IF EXISTS Viitteet;
CREATE TABLE Viitteet (
    id SERIAL PRIMARY KEY,
    viite TEXT,
    tyyppi TEXT,
    vuosi INTEGER,
    kirjailija TEXT,
    otsikko TEXT,
    kustantaja TEXT,
    versio INTEGER,
    julkaisunumero TEXT,
    sivut TEXT
);