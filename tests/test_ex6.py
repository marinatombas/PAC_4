"""
Mòdul de proves unitàries per l'exercici 6.
"""
import pandas as pd
from exercises.ex6 import fun_total_goals

def test_fun_total_goals():
    """
    Test unitari per verificar que fun_total_goals calcula correctament
    la suma de gols locals, visitants i totals.

    """
    # 1. Creem conjunt de dades 
    mock_data = pd.DataFrame({
        "FTHG": [2, 1, 3],  # Suma gols locals = 6
        "FTAG": [1, 0, 2]   # Suma gols visitants = 3
    })

    # 2. Executem la funció amb les nostres dades
    home_goals, away_goals, total_goals = fun_total_goals(mock_data)

    # 3. Comprovem si els resultats són els esperats
    assert home_goals == 6, f"S'esperaven 6 gols locals, s'han obtingut {home_goals}"
    assert away_goals == 3, f"S'esperaven 3 gols visitants, s'han obtingut {away_goals}"
    assert total_goals == 9, f"S'esperaven 9 gols totals, s'han obtingut {total_goals}"