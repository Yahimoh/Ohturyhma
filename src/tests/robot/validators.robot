*** Settings ***
Resource  resource.robot
Suite Setup  Avaa Ja Konfiguroi Selain
Suite Teardown  Close Browser
Test Setup  Mene Sivustolle

*** Variables ***
${PITKA_SYOTE}    ${'a'*101}

*** Test Cases ***


Liian suuren syötteen lisääminen aiheuttaa virheilmoituksen
    Aseta Kirjailija  ${PITKA_SYOTE}
    Aseta Otsikko  testiotsikko
    Aseta Vuosi  2023
    Aseta Kustantaja  testikustantaja
    Lisää Kirjan Tiedot
    Page Should Contain  Kentän 'kirjailija' syöte tulee olla vähintään 1 ja enintään 100 merkkiä pitkä!


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