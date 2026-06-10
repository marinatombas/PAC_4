"""Mòdul pel càlcul i visualització de partits guanyats a casa / fora.
Correspon a l'exercici 4."""

import pandas as pd
import matplotlib.pyplot as plt
import config

def FTR(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el nombre de victòries locals,
    victòries visitants i empats.

    Args:
        data (pd.DataFrame): Conjunt de dades dels partits.

    Returns:
        pd.DataFrame:
            Resultats totals dels partits.
    """

    # Comptar resultats
    results = data["FTR"].value_counts()
    labels = {
        "H": "H: Guanya local",
        "A": "A: Guanya visitant",
        "D": "D: Empat"
    }
    # Convertir a DataFrame
    ftr = pd.DataFrame({
        "Resultat": [labels[x] for x in results.index],
        "Partits": results.values
    })

    return ftr

def plot_FTR(ftr: pd.DataFrame) -> None:
    """
    Representa el nombre de victòries locals,
    visitants i empats.

    La figura es guarda a la carpeta img/.

    Args:
        ftr (pd.DataFrame):
            DataFrame amb els resultats totals.
    """

    plt.figure(figsize=(6, 5))

    plt.bar(
        ftr["Resultat"],
        ftr["Partits"]
    )
    plt.xlabel("Resultat")
    plt.ylabel("Nombre de partits")

    plt.title("Distribució de resultats finals")

    plt.tight_layout()

    plt.savefig(
        f"img/grafica_ex4_{config.nom_alumne}_{config.date_time}.png"
    )

    # Mostrar en pantalla (Comentat ja que s'ha preferit que no ho mostri)
    # plt.show()
