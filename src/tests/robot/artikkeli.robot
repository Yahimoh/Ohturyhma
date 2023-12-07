*** Settings ***
Resource  resource.robot
Suite Setup  Avaa Ja Konfiguroi Selain
Suite Teardown  Close Browser
Test Setup  Mene Sivustolle

*** Test Cases ***
Sivu On Auki
    Sivuston Pitäisi Olla Auki

Lisaa Artikkeliviite
    Sivuston Pitäisi Olla Auki
    Valitse Artikkeliviite
    Aseta Kirjailija  testikirjailija
    Aseta Otsikko  testiotsikko
    Aseta Vuosi  2023
    Aseta Kustantaja  testikustantaja
    Aseta Julkaisunumero  3
    Aseta Sivut  14-15
    Lisää Artikkelin Tiedot
    Page Should Contain  testikirjailija

Viitteen voi nähdä nappia painamalla bibtex muodossa
    Sivuston Pitäisi Olla Auki
    Näytä Bibtex Nappia Painetaan
    BibTex Muoto Näkyy

*** Keywords ***
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

Aseta Julkaisunumero
    [Arguments]  ${julkaisunumero}
    Input Text  julkaisunumero  ${julkaisunumero}

Aseta Sivut
    [Arguments]  ${sivut}
    Input Text  sivut  ${sivut}

Lisää Artikkelin Tiedot
    Click Button  Lisää

Näytä Bibtex Nappia Painetaan
    Click button  Näytä BibTex

BibTex Muoto Näkyy
    Page Should Contain  Piilota BibTex

Valitse Artikkeliviite
    Click Button  Artikkeliviite