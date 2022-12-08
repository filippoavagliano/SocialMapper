# SocialMapper


La versione di Python utilizzata è: **3.10.6**.

Scaricare i pesi delle reti neurali mediante lo script `init.sh` (Linux) o `init.bat` (Windows). 
Lo script contiene anche le immagini di input e gli output dei casi di studio. Per la rete **Logohunter** sono presenti i 
risultati sia con due varianti dello stesso logo (nella cartella *logohunter_2*), sia con sette; quest'ultimi sono utilizzati 
per l'output finale. È preferibile fare uso della variante a due loghi se non si dispone di almeno 16GB di RAM.

```sh
./init.sh
```

```bat
init.bat
```

Installare i requisiti definiti in `requirements.txt` (Linux) o `windows_requirements.txt` (Windows) in un ambiente virtuale.

``` sh
pip install -r requirements.txt
```

``` sh
pip install -r windows_requirements.txt
```

Le credenziali dell'account Instagram con cui eseguire il login per scaricare le immagini sono configurabili dal file `credentials.yaml`. 
A causa dei nuovi controlli introdotti da Instagram potrebbe essere necessario inserire il codice di controllo inviato
alla mail corrispondente all'account.

