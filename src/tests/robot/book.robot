*** Settings ***
Resource  resource.robot
Suite Setup  Avaa Ja Konfiguroi Selain
Suite Teardown  Close Browser
Test Setup  Mene Sivustolle

*** Test Cases ***
Sivu On Auki
    Sivuston Pitäisi Olla Auki
Lisaa Kirjaviite
    Sivuston Pitäisi Olla Auki
    Aseta Kirjailija  testikirjailija
    Aseta Otsikko  testiotsikko
    Aseta Vuosi  2023
    Aseta Kustantaja  testikustantaja
    Lisää Kirjan Tiedot
    Page Should Contain  testikirjailija

Viitteen voi nähdä nappia painamalla bibtex muodossa
    Sivuston Pitäisi Olla Auki
    Näytä Bibtex Nappia Painetaan
    BibTex Muoto Näkyy

Aluksi viitteitä ei näytetä BibTex muodossa
    Sivuston Pitäisi olla Auki
    Page Should Not Contain  Piilota BibTex

Tunniste generoituu oikein
    Page Should Contain  t23

Kaikkien viiteiden kopiointi leikepöydälle onnistuu
    Sivuston Pitäisi Olla Auki
    Kopioi Kaikki Viitteet Leikepöydälle Nappia Painetaan
    Alert Should Be Present  Kaikki viitteet on kopioitu leikepöydälle!

*** Keywords ***
Aseta Viite
    [Arguments]  ${viite}
    Input text  viite  ${viite}

Aseta Kirjailija
    [Arguments]  ${kirjailija}
    Input text  kirjailija  ${kirjailija}

Aseta Otsikko
    [Arguments]  ${otsikko}
    Input text  otsikko  ${otsikko}

Aseta Vuosi
    [Arguments]  ${vuosi}
    Input text  vuosi  ${vuosi}

Aseta Kustantaja
    [Arguments]  ${kustantaja}
    Input text  kustantaja  ${kustantaja}

Lisää Kirjan Tiedot
    Click Button  Lisää

Näytä Bibtex Nappia Painetaan
    Click Button  Näytä BibTex

BibTex Muoto Näkyy
    Page Should Contain  Piilota BibTex


Kopioi Kaikki Viitteet Leikepöydälle Nappia Painetaan
    Click Button  Kopioi kaikki viitteet leikepöydälle