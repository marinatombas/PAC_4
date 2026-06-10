"""Mòdul pel càlcul del Dataframe summary_1995_2025 i
 visualització del Pòdium. Correspon a l'exercici 6."""

import pandas as pd
import matplotlib.pyplot as plt
import config

def fun_total_goals(
        data: pd.DataFrame
) -> tuple[int, int, int]:
    """
    Calcula els gols totals marcats.

    Args:
        data (pd.DataFrame): Conjunt de dades dels partits.

    Returns:
        tuple[int, int, int]:
            Gols locals, visitants i totals.
    """

    home_goals = int(data["FTHG"].sum())

    away_goals = int(data["FTAG"].sum())

    total_goals = home_goals + away_goals

    return home_goals, away_goals, total_goals


def fun_total_goals_by_team(
        data: pd.DataFrame
) -> tuple[
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame
]:
    """
    Calcula els gols totals per equip.

    Args:
        data (pd.DataFrame): Conjunt de dades dels partits.

    Returns:
        tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
            Gols locals, visitants i totals per equip.
    """

    # Gols com a local
    home_goals = data.groupby("HomeTeam")[
        "FTHG"
    ].sum()

    home_goals_by_team = pd.DataFrame({
        "Equip": home_goals.index,
        "GolsLocal": home_goals.values
    })

    # Gols com a visitant
    away_goals = data.groupby("AwayTeam")[
        "FTAG"
    ].sum()

    away_goals_by_team = pd.DataFrame({
        "Equip": away_goals.index,
        "GolsVisitant": away_goals.values
    })

    # Gols Total
    total_goals = home_goals + away_goals


    total_goals_by_team = pd.DataFrame({
        "Equip": total_goals.index,
        "GolsTotals": total_goals.values
    })

    return (
        home_goals_by_team,
        away_goals_by_team,
        total_goals_by_team
    )

def fun_summary_1996_2025(
        df_total_points: pd.DataFrame,
        home_goals_by_team: pd.DataFrame,
        away_goals_by_team: pd.DataFrame,
        total_goals_by_team: pd.DataFrame
) -> pd.DataFrame:
    """
    Crea el dataframe resum global.

    Args:
        df_total_points (pd.DataFrame):
            Punts totals.

        home_goals_by_team (pd.DataFrame):
            Gols locals.

        away_goals_by_team (pd.DataFrame):
            Gols visitants.

        total_goals_by_team (pd.DataFrame):
            Gols totals.

    Returns:
        pd.DataFrame:
            DataFrame resum.
    """

    summary = df_total_points.merge(
        home_goals_by_team,
        on="Equip"
    )

    summary = summary.merge(
        away_goals_by_team,
        on="Equip"
    )

    summary = summary.merge(
        total_goals_by_team,
        on="Equip"
    )

    return summary

def podium(summary_1996_2025: pd.DataFrame) -> None:
    """
    Crea una grafica de pòdium històric dels equips.

    Args:
         summary_1996_2025 (pd.DataFrame): DataFrame resum.
    """
    top3 = (summary_1996_2025.sort_values(
        by="Punts",
        ascending=False
    )).head(3)

    primer = top3.iloc[0]
    segon = top3.iloc[1]
    tercer = top3.iloc[2]

    podi = [segon["Equip"], primer["Equip"], tercer["Equip"]]

    altura = [2, 3, 1]

    posicions = [0, 1, 2]

    # Colors podium
    colors = ["silver", "gold", "#CD7F32"]

    plt.figure(figsize=(8, 6))
    plt.bar(
        posicions,
        altura,
        color=colors
    )
    # Noms dels equips
    for i, equip in enumerate(podi):
        plt.text(
            posicions[i],
            altura[i] + 0.1,
            equip,
            ha="center",
        )

    plt.xticks([])
    plt.yticks([])

    plt.ylim(0, 4)
    plt.xlim(-0.5, 2.5)

    plt.title("Pòdium històric")

    plt.savefig(
        f"img/grafica_ex6_{config.nom_alumne}_{config.date_time}.png"
    )

    # Mostrar en pantalla (Comentat ja que s'ha preferit que no ho mostri)
    #plt.show()
