*** Settings ***

Library Selenium2Library

Library sample.py.Customlib
*** Test Case ***
google test

Open Broweser https://www.google.com
Maximize Browser Window

${SEARCH} = time_date

Imput text id=lts-ib ${SEARCH}
sleep 5
Close Browser
