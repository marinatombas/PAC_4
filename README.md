# PAC4 - Anàlisi Històrica LaLiga 1995-2025
## Autora
**Marina Tombas Suñé**


## Descripció del projecte

Aquest projecte analitza dades històriques de LaLiga entre 1995 i 2025 mitjançant Python.

El projecte inclou:

- Anàlisi de dades
- Visualitzacions
- Càlcul de classificacions històriques
- Grafs de connexions entre equips
- Documentació
- Tests automatitzats

## Estructura del projecte
L'organització de fitxers i carpetes segueix l'estructura professional requerida per a la pràctica:
```text
PAC_4_MARINA_TOMBAS_SUÑÉ/
│
├── doc/                       # Documentació en HTML generada automàticament
├── tests/                     # Proves unitàries del projecte
│   └── test_ex6.py            # Test de la funció fun_total_goals
│
├── screenshots/               # Captures que demostren l'autoria de la pac
│
├── src/                       # Codi font de l'aplicació
│   ├── data/                  # Conté els fitxers de dades d'entrada (LaLiga_Matches.csv)
│   ├── exercises/             # Mòduls corresponents a cada exercici (ex1 a ex7)
│   │   ├── ex1.py
│   │   └── ...
│   ├── img                    # Conté les imatges generades a l'executar el codi
│   ├── main.py                # Punt d'entrada del programa principal
│   ├── config.py              # Configuració, conté les variables nom_alumne i date_time
│   └── .pylintrc              # Fitxer de configuració del linter Pylint
│
├── LICENSE                    # Llicència de distribució MIT
├── README.md                  # Documentació bàsica del projecte
└── requirements.txt           # Dependències del projecte
```

## Instal·lació del projecte

Per aixecar el projecte des de zero en un entorn virtual net de Python cal seguir els següents passos des de la terminal.
Crear un entorn virtual:

1. Crear l'entorn virtual
    ```bash
    python -m venv .venv
2. Activar l'entorn virtual:
   * A Windows
       ```bash
       .venv\Scripts\Activate.ps1
   * A Linux / macOS:
       ```bash
       source .venv/bin/activate
3. Instal·lar les dependències de producció requerides:
     ```bash
   pip install -r requirements.txt
Nota: El fitxer requirements no inclou les llibreries associades al linting, documentació o tests.

## Execució del projecte

El fitxer principal main.py actua com a punt d'entrada seqüencial mitjançant arguments per terminal.
Per executar-lo, navegueu primer a la carpeta `src/`:
* ```bash
    cd src
A continuació:
* Mostrar ajuda de l'script:
    ```bash
    python main.py -h
* Execució incremental d'exercicis (Exemple per executar fins a l'exercici 6):
    ```bash
    python main.py -ex 6

## Qualitat del Codi (Linting)

Per verificar la qualitat de l'estil de codi i el compliment de la guia PEP 8, s'ha utilitzat l'eina **Pylint**. 
El criteri de revisió s'ha adaptat mitjançant el fitxer de configuració `.pylintrc` per ometre restriccions excessives 
sobre el nombre de variables locals o noms de funcions específiques del domini (ex: `FTR`).

Per comprovar el linting del projecte, executeu les següents comandes a la terminal des de la carpeta arrel:

1. Navegueu fins a la carpeta src del projecte (on es troben el fitxer main.py i el fitxer .pylintrc):
    ```bash
    cd src
    
2. Instal·lar Pylint (si no està instal·lat):
   ```bash
   pip install pylint
   
3. Executar l'anàlisi sobre el fitxer principal i els mòduls:
   ```bash
   pylint main.py exercises/

## Documentació del codi (Exercici 10)
La documentació del projecte s'ha generat automàticament a partir dels *docstrings* de cada funció utilitzant la llibreria 
nativa **pydoc**. Els fitxers resultants en format HTML es troben emmagatzemats a la carpeta `doc/` de l'arrel del projecte.

Per tornar a generar la documentació des de zero, seguiu aquests passos des de la terminal a l'arrel del projecte:
   1. Assegureu-vos de trobar-vos a la carpeta arrel (`PAC_4_MARINA_TOMBAS_SUÑÉ\src`). 
   2. Executeu la següent comanda per generar els fitxers HTML de tots els mòduls:
      ```bash
      python -m pydoc -w exercises.ex1 exercises.ex2 exercises.ex3 exercises.ex4 exercises.ex5 exercises.ex6 exercises.ex7 main


## Execució de Tests Unitaris (Ex 11)

S'ha implementat un test unitari utilitzant el framework **pytest** per validar el funcionament de la funció `fun_total_goals` de l'exercici 6.
La carpeta de tests es troba estructurada a l'arrel del projecte.

Per executar les proves unitàries correctament, seguiu els següents passos des de la terminal:
1. Instal·leu el framework de proves:
   ```bash
   pip install pytest
   
2. Assegureu-vos d'estar a la carpeta arrel del projecte (`PAC_4_MARINA_TOMBAS_SUÑÉ`) i amb l'entorn virtual actiu.
3. Indiqueu el camí del codi font (src) i executeu la suite de tests amb la comanda corresponent al vostre sistema operatiu:

* A Windows:
    ```bash
   $env:PYTHONPATH="src"; python -m pytest tests/

* A macOS/ Linux:
    ```bash
    PYTHONPATH=src python3 -m pytest tests/

## Comandes per pujar el projecte a GitHub

Per tal de pujar el projecte a GitHub des del terminal, se segueix la seqüència de comandes:
1. Incicialitzar el repositori local de Git
    ```bash
    git init
2. Afegir els fitxers al sistema de control de versions
    ```bash
    git add .
3. Crear el commit amb els fitxers
    ```bash
   git commit -m "Initial commit: Estructura completa de la PAC4 de LaLiga"
4. Configurar la branca principal per defecte:
    ```bash
   git branch -M main
5. Enllaçar el repositori local amb el de GitHub (En aquest cas s'afegeix el meu git):
    ```
   git remote add origin https://github.com/marinatombas/PAC_4.git
6. Pujar el codi final a la plataforma
   ```bash
   git push -u origin main
