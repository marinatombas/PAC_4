"""Mòdul pel càlcul i visualització de partits totals jugats.
Correspon a l'exercici 2."""

import pandas as pd
import matplotlib.pyplot as plt
import config

def total_matches(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula el nombre total de partits jugats per equip.

    Args:
        data (pd.DataFrame): Conjunt de dades de partits.

    Returns:
        pd.DataFrame: DataFrame amb equips i partits totals.
    """

    # Partits locals
    home_matches = data["HomeTeam"].value_counts()

    # Partits visitants
    away_matches = data["AwayTeam"].value_counts()

    # Total
    total = home_matches + away_matches

    # Convertir a DataFrame
    matches_team_total = pd.DataFrame({
        "Equip": total.index,
        "PartitsTotals": total.values
    })

    return matches_team_total

def plot_matches_team_total(
        matches_team_total: pd.DataFrame
) -> None:
    """
    Representa el nombre total de partits jugats
    per cada equip.

    La figura es guarda a la carpeta img/.

    Args:
        matches_team_total (pd.DataFrame):
            DataFrame amb els partits totals per equip.
    """
    plt.figure(figsize=(14, 6))

    plt.bar(
        matches_team_total["Equip"],
        matches_team_total["PartitsTotals"]
    )

    plt.xticks(rotation=90)

    plt.xlabel("Equips")
    plt.ylabel("Partits totals")

    plt.title("Partits totals jugats per equip")

    plt.tight_layout()

    plt.savefig(
        f"img/grafica_ex2_{config.nom_alumne}_{config.date_time}.png"
    )

    # Mostrar en pantalla (Comentat ja que s'ha preferit que no ho mostri)
    # plt.show()
