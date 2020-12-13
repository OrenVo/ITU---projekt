# ITU Projekt 2020: README

## Tým: DeusVult!
## Projekt: Automatický vypínač pre dektopovú a webovú aplikáciu

### Súbory

#### (1.) Inštalačný súbor
install.sh

#### (2.) Licencia
LICENSE

#### (3.) Hlavný súbor serveru
main.py

#### (4.) Readme
README.md

#### (5.) Konfiguračná zložka
conf
    &nbsp;&nbsp;&nbsp;- rights.conf

#### (6.) Konfiguračná zložka
config
    &nbsp;&nbsp;&nbsp;- rights.conf

#### (7.) Zdrojové súbory beckend serveru
src
    &nbsp;&nbsp;&nbsp;- monitor_status.sh
    &nbsp;&nbsp;&nbsp;- requierements.txt
    &nbsp;&nbsp;&nbsp;- resourse_monitor.py
    &nbsp;&nbsp;&nbsp;- shared.py
    &nbsp;&nbsp;&nbsp;- timer.py
    &nbsp;&nbsp;&nbsp;-> __pychace_
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- resource_monitor.cpython-38
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- shared.cpython-38.pyc
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- timer.cpython-38.pyc
    

#### (8.) Statické súbory pre Web aplikáciu
static
    &nbsp;&nbsp;&nbsp;-> css
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- index_style.css
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- login_style.css
    &nbsp;&nbsp;&nbsp;- pictures

#### (9.) Html súbory pre Web aplikáciu
templates
    &nbsp;&nbsp;&nbsp;- index.html
    &nbsp;&nbsp;&nbsp;- login.html

### Spustenie

#### (1.) Požiadavky
Pre úspšné spustenie je nutné mať nainštalované všetky požiadavky v súbore *requierements.txt*.

Inštalácia požiadavkov pomocou príkazu:
*pip3 install -r requierements.txt*

#### (2.) Spustenie servera
Spustenie servera:
*python3 main.py*
*Pozn. je nutné mať práva superužívateľa.*

### Desktopová aplikácia
TODO

### Webová aplikácia
Použitie webovej aplikácie.

##### (1.) Vzdialený server
Je nutné sa pripojiť na vzdialený server pomocou príkazu:
*ssh name@servername*

##### (2.) Spustenie
Spustenie cez webový prehliadač na adrese:
*localhost:5000* alebo *127.0.0.1:5000*

##### (3.) Prihlásenie a spustenie aplikácie
Po pripojení na vybraný server a spustení aplikácie v prehliadači sa musíte prihlásiť. Po prihlásení sa vám zobrazí stránka na ktorej môžete nastaviť ktoré akcie sa vykonajú a spustiť aplikáciu.
