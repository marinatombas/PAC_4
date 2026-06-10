"""Mòdul per a la càrrega de dades i visualització de la
distribució de gols inicial. Correspon a l'exercici 1."""

import pandas as pd
import matplotlib.pyplot as plt
import config

def load_and_eda(file: str) -> pd.DataFrame:
    """
    Carrega el conjunt de dades, elimina columnes innecessàries
    i mostra informació bàsica.

    Args:
        file (str): Ruta del CSV.

    Returns:
        pd.DataFrame: Dataset processat.
     """

    # Carreguem dades

    df = pd.read_csv(file)

    # Eliminem columnes
    cols_remove = ["HTHG", "HTAG", "HTR"]
    data = df.drop(cols_remove, axis=1)

    # Mostrar informació
    print("\n *** PRIMERES FILES ***")
    print(data.head())

    print("\n *** ÚLTIMES FILES ***")
    print(data.tail())

    print("\n *** INFO DATASET ***")
    data.info()

    print("\n *** DESCRIPCIÓ ***")
    print(data.describe())

    return data

def plot_home_away_goals(data) -> None:
    """
    Mostra la distribució de gols dels equips locals
    i visitants mitjançant box-plots.

    La figura es guarda a la carpeta img/.

    Args:
        data (pd.DataFrame): Conjunt de dades dels partits.
    """

    _, axes = plt.subplots(1, 2, figsize=(10, 5))

    # Gols locals
    axes[0].boxplot(data["FTHG"])
    axes[0].set_title("Gols equips locals")

    # Gols visitants
    axes[1].boxplot(data["FTAG"])
    axes[1].set_title("Gols equips visitants")

    plt.tight_layout()

    # Guardar figura
    plt.savefig(
        f"img/grafica_ex1_{config.nom_alumne}_{config.date_time}.png"
    )

# Mostrar en pantalla (Comentat ja que s'ha preferit que no ho mostri)
# plt.show()
