"""Mòdul pel càlcul de la classificació històrica 1995 - 2025.
Correspon a l'exercici 5."""

import pandas as pd

def add_points(data: pd.DataFrame) -> pd.DataFrame:
    """
    Afegeix els punts aconseguits
    pels equips locals i visitants.

    Args:
        data (pd.DataFrame): Conjunt de dades dels partits.

    Returns:
        pd.DataFrame:
            Dataset amb les noves columnes
            points_home i points_away.
    """


    # Inicialitzar columnes
    data["points_home"] = 0
    data["points_away"] = 0

    # Victòria local
    data.loc[data["FTR"] == "H", "points_home"] = 3
    data.loc[data["FTR"] == "H", "points_away"] = 0

    # Victòria visitant
    data.loc[data["FTR"] == "A", "points_home"] = 0
    data.loc[data["FTR"] == "A", "points_away"] = 3

    # Empat
    data.loc[data["FTR"] == "D", "points_home"] = 1
    data.loc[data["FTR"] == "D", "points_away"] = 1

    return data


def fun_total_points(
        data: pd.DataFrame
) -> tuple[pd.Series, pd.DataFrame]:
    """
    Calcula els punts totals acumulats
    per cada equip.

    Args:
        data (pd.DataFrame): Conjunt de dades dels partits.

    Returns:
        tuple[pd.Series, pd.DataFrame]:
            Series i DataFrame amb els punts totals.
    """

    # Punts com a local
    home_points = data.groupby("HomeTeam")[
        "points_home"
    ].sum()

    # Punts com a visitant
    away_points = data.groupby("AwayTeam")[
        "points_away"
    ].sum()

    # Suma total
    total_points = home_points + away_points

    # Ordenar
    total_points = total_points.sort_values(
        ascending=False
    )

    # Convertir a DataFrame
    df_total_points = pd.DataFrame({
        "Equip": total_points.index,
        "Punts": total_points.values
    })

    return total_points, df_total_points

def alltime_winner(
        df_total_points: pd.DataFrame
) -> str:
    """
    Retorna l'equip amb més punts històrics.

    Args:
        df_total_points (pd.DataFrame):
            DataFrame amb punts totals.

    Returns:
        str: Equip guanyador històric.
    """

    winner = df_total_points.iloc[0]["Equip"]

    return winner
