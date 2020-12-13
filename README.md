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
conf  <br />
    &nbsp;&nbsp;&nbsp;- rights.conf

#### (6.) Konfiguračná zložka
config  <br />
    &nbsp;&nbsp;&nbsp;- rights.conf

#### (7.) Zdrojové súbory beckend serveru
src  <br />
    &nbsp;&nbsp;&nbsp;- monitor_status.sh  <br />
    &nbsp;&nbsp;&nbsp;- requierements.txt  <br />
    &nbsp;&nbsp;&nbsp;- resourse_monitor.py  <br />
    &nbsp;&nbsp;&nbsp;- shared.py  <br />
    &nbsp;&nbsp;&nbsp;- timer.py  <br /> 
    &nbsp;&nbsp;&nbsp;-> __pychace_  <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- resource_monitor.cpython-38  <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- shared.cpython-38.pyc  <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- timer.cpython-38.pyc  <br />
    

#### (8.) Statické súbory pre Web aplikáciu
static  <br />
    &nbsp;&nbsp;&nbsp;-> css  <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- index_style.css  <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- login_style.css  <br />
    &nbsp;&nbsp;&nbsp;- pictures  <br />

#### (9.) Html súbory pre Web aplikáciu
templates  <br />
    &nbsp;&nbsp;&nbsp;- index.html  <br />
    &nbsp;&nbsp;&nbsp;- login.html  <br />

### Spustenie

#### (1.) Požiadavky
Pre úspšné spustenie je nutné mať nainštalované všetky požiadavky v súbore *requierements.txt*.

Inštalácia požiadavkov pomocou príkazu:  <br />
*pip3 install -r requierements.txt*

#### (2.) Spustenie servera
Spustenie servera:  <br />
*python3 main.py*  <br />
*Pozn. je nutné mať práva superužívateľa.*  

### Desktopová aplikácia
TODO

### Webová aplikácia
Použitie webovej aplikácie.

##### (1.) Vzdialený server
Je nutné sa pripojiť na vzdialený server pomocou príkazu:  <br />
*ssh name@servername*

##### (2.) Spustenie
Spustenie cez webový prehliadač na adrese:  <br />
*localhost:5000* alebo *127.0.0.1:5000*

##### (3.) Prihlásenie a spustenie aplikácie
Po pripojení na vybraný server a spustení aplikácie v prehliadači sa musíte prihlásiť. Po prihlásení sa vám zobrazí stránka na ktorej môžete nastaviť ktoré akcie sa vykonajú a spustiť aplikáciu.
