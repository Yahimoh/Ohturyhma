*** Settings ***
Library  AppLibrary
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${DELAY}  0.5 seconds
${HOME_URL}  http://${SERVER}

*** Keywords ***
Avaa Ja Konfiguroi Selain
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method  ${options}  add_argument  --no-sandbox
    #Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Mene Sivustolle
    Go To  ${HOME_URL}

Sivuston Pitäisi Olla Auki
    Title Should Be  Lähdeviitteet
