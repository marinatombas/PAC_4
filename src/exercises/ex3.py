"""Mòdul pel càlcul i visualització de la distribució
de gols. Correspon a l'exercici 3."""

import pandas as pd
import matplotlib.pyplot as plt
import config

def goals_distribution(
        data: pd.DataFrame
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Calcula la distribució de gols marcats
    pels equips locals i visitants.

    Args:
        data (pd.DataFrame): Conjunt de dades dels partits.

    Returns:
        tuple[pd.DataFrame, pd.DataFrame]:
            Distribució de gols locals i visitants.
    """
    # Distribució gols locals
    home_goals = data["FTHG"].value_counts().sort_index()

    distr_goals_home = pd.DataFrame({
        "Gols": home_goals.index,
        "Partits": home_goals.values
    })

    # Distribució gols visitants
    away_goals = data["FTAG"].value_counts().sort_index()

    distr_goals_away = pd.DataFrame({
        "Gols": away_goals.index,
        "Partits": away_goals.values
    })

    return distr_goals_home, distr_goals_away

def plot_goals_distribution(
        distr_goals_home: pd.DataFrame,
        distr_goals_away: pd.DataFrame
) -> None:
    """
    Representa la distribució de gols marcats
    pels equips locals i visitants.

    La figura es guarda a la carpeta img/.

    Args:
        distr_goals_home (pd.DataFrame):
            Distribució de gols locals.

        distr_goals_away (pd.DataFrame):
            Distribució de gols visitants.
    """

    _, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Gols locals
    axes[0].bar(
        distr_goals_home["Gols"],
        distr_goals_home["Partits"]
    )

    axes[0].set_title("Gols equips locals")
    axes[0].set_xlabel("Nombre de gols")
    axes[0].set_ylabel("Nombre de partits")

    # Gols visitants
    axes[1].bar(
        distr_goals_away["Gols"],
        distr_goals_away["Partits"]
    )

    axes[1].set_title("Gols equips visitants")
    axes[1].set_xlabel("Nombre de gols")
    axes[1].set_ylabel("Nombre de partits")

    plt.tight_layout()

    plt.savefig(
        f"img/grafica_ex3_{config.nom_alumne}_{config.date_time}.png"
    )

    # Mostrar en pantalla (Comentat ja que s'ha preferit que no ho mostri)
    # plt.show()
