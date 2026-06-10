"""
Mòdul principal del projecte d'anàlisi de dades de LaLiga.

Aquest script llegeix els paràmetres de la terminal per executar de
forma incremental els diferents mòduls i gràfics de la pràctica.
"""

import sys
from exercises.ex1 import load_and_eda, plot_home_away_goals
from exercises.ex2 import total_matches, plot_matches_team_total
from exercises.ex3 import goals_distribution, plot_goals_distribution
from exercises.ex4 import FTR, plot_FTR
from exercises.ex5 import add_points, alltime_winner, fun_total_points
from exercises.ex6 import fun_total_goals, fun_summary_1996_2025, fun_total_goals_by_team, podium
from exercises.ex7 import graf

def show_help() -> None:
    """
    Mostra ajuda d'execució
    """

    print("\nÚs:")
    print("python main.py -ex NUM")

    print("\nArguments:")
    print("-ex Número d'exercicis a executar")

    print("\nExemple:")
    print("python main.py -ex 5")


def main():
    """
    Funció principal que actua com a punt d'entrada de l'aplicació.
    :return: none
    """
    # Help
    if "-h" in sys.argv or "--help" in sys.argv:
        show_help()
        return

    # Validar arguments
    if "-ex" not in sys.argv:
        print("Error: cal indicar -ex NUM")
        return

    try:
        ex_index = sys.argv.index("-ex")
        ex = int(sys.argv[ex_index + 1])

    except (ValueError, IndexError):
        print("Error en l'argument -ex")

        return

    # Exercici 1
    data = load_and_eda("data/LaLiga_Matches.csv")

    if ex >= 1:
        plot_home_away_goals(data)

    # Exercici 2
    if ex >= 2:
        matches_team_total  = total_matches(data)
        print("\n *** Primers 10 Equips del DataFrame ***")
        print(matches_team_total.head(10))

        #Màxim nombre de partits
        max_match  = matches_team_total["PartitsTotals"].max()

        equips_primera =  matches_team_total[
        matches_team_total["PartitsTotals"] == max_match
        ]

        print("\n *** Equips primera divisió ***")
        print(equips_primera)

        plot_matches_team_total(matches_team_total)

    # Exercici 3
    if ex >= 3:
        distr_goals_home, distr_goals_away = goals_distribution(data)

        print("\n *** DISTRIBUCIÓ GOLS LOCALS *** ")
        print(distr_goals_home)

        print("\n *** DISTRIBUCIÓ GOLS VISITANTS *** ")
        print(distr_goals_away)

        plot_goals_distribution( distr_goals_home,distr_goals_away)

    # Exercici 4
    if ex >= 4:

        ftr = FTR(data)
        print("\n *** RESULTATS PARTITS  *** ")
        print(ftr)

        # Percentatges
        guanyats_casa = ftr.loc[
            ftr["Resultat"] == "H: Guanya local",
            "Partits"
        ].values[0]
        total = ftr["Partits"].sum()
        percentatge_casa = (guanyats_casa / total) * 100
        print(
            f"\nPercentatge victòries locals: "
            f"{percentatge_casa:.2f}%"
        )
        plot_FTR(ftr)

    # Exercici 5

    if ex >= 5:
        data = add_points(data)

        print("\n *** DATASET AMB PUNTS *** ")
        print(data.head(10))

        _, df_total_points = fun_total_points(data)
        print("\n *** TOP 10 PUNTS HISTÒRICS ***")
        print(df_total_points.head(10))

        winner = alltime_winner(df_total_points)

        print("\n *** GUANYADOR HISTÒRIC ***")
        print(f"L'equip guanyador de la lliga històrica acomulada és el {winner}")

    # Exercici 6

    if ex >= 6:
        home_goals, away_goals, total_goals = (
            fun_total_goals(data)
        )
        print("\n *** GOLS TOTALS *** ")
        print(f"Gols locals: {home_goals}")
        print(f"Gols visitants: {away_goals}")
        print(f"Gols totals: {total_goals}")

        (
            home_goals_by_team,
            away_goals_by_team,
            total_goals_by_team
        ) = fun_total_goals_by_team(data)

        print("\n *** TOP 10 GOLS ***")
        print(total_goals_by_team.head(10))

        summary_1996_2025 = fun_summary_1996_2025(
            df_total_points,
            home_goals_by_team,
            away_goals_by_team,
            total_goals_by_team
        )

        print("\n *** SUMMARY ***")
        print(summary_1996_2025.head())

        podium(summary_1996_2025)

    # Exercici 7

    if ex >= 7:

        equips_millors = df_total_points.sort_values(
            by="Punts",
            ascending=False
        ).head(5)["Equip"].tolist()

        print(f"Els 5 millors equips son {equips_millors}")

        graf(data, equips_millors)


if __name__ == "__main__":
    main()
