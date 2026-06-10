"""Mòdul per la representació d'un graf. Correspon a l'exercici 7."""

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import config

def graf(
        data: pd.DataFrame,
        selected_teams: list[str]
) -> None:
    """
    Genera un graf de conexions entre equips.

    Args:
        data (pd.DataFrame): Conjunt de dades dels partits.
        selected_teams (list [str]): Llista d'equips seleccionats.
    """

    # Filtrar partits entre equips

    filtrat = data[
        (data["HomeTeam"].isin(selected_teams)) &
        (data["AwayTeam"].isin(selected_teams))
    ]

    conexions = filtrat.groupby(["HomeTeam", "AwayTeam"]).size()

    # Graf
    G = nx.Graph()

    # Nodes
    for team in selected_teams:
        G.add_node(team)

    # Arestes
    for (home, away), count in conexions.items():

        if G.has_edge(home, away):
            G[home][away]["weight"] += count

        else:
            G.add_edge(home, away, weight = count)

    # Posició
    pos = nx.spring_layout(G, seed = 1999)

    plt.figure(figsize = (10, 8))

    nx.draw_networkx_nodes(G, pos, node_size = 200, node_color = "black")

    label_pos = {
        node: (x, y + 0.1)
        for node, (x, y) in pos.items()
    }

    nx.draw_networkx_labels(
        G,
        label_pos,
        font_size=14
    )
    nx.draw_networkx_edges(G, pos)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels)

    plt.title("Graf de conexions entre equips")

    plt.axis("off")

    plt.savefig(f"img/graf_{config.nom_alumne}_{config.date_time}.png")

    # Mostrar en pantalla (Comentat ja que s'ha preferit que no ho mostri)
    # plt.show()
