import networkx as nx
from random import random, choice, randint


def create_base_random_graph(number_of_nodes: int=1000,
                             p_conn: float=0.01,
                             min_path_length: int=3,
                             weight_distribution=lambda : random() + 1,
                             debug: bool=False,
                             *args, **kwargs) -> nx.Graph:
    """

    :param number_of_nodes:
    :param p_conn:
    :param min_path_length:
    :param weight_distribution:
    :param args:
    :param kwargs:
    :return:
    """
    while True:
        G = nx.Graph()
        G.add_nodes_from(range(number_of_nodes))
        SOURCE = 0
        TARGET = 1
        for n in G.nodes():
            for m in G.nodes():
                if m <= n:
                    continue
                if random() < p_conn:
                    G.add_edge(
                        u_of_edge=n,
                        v_of_edge=m,
                        weight=weight_distribution()
                    )
                # End of m in G.nodes()
            # End of n in G.nodes()

        def get_paths():
            PATHS = [
                P for P in nx.all_simple_paths(
                    G=G,
                    source=SOURCE,
                    target=TARGET,
                    cutoff=min_path_length-1
                )
            ]
            return PATHS

        PATHS = get_paths()

        while len(PATHS) > 0:
            for path in PATHS:
                print(f"Path: {path}")
                source_idx = randint(0, len(path)-2)
                print(source_idx)
                source = path[source_idx]
                target = path[source_idx+1]
                G.remove_edge(u=source, v=target)

            PATHS = get_paths()

        if nx.is_connected(G):
            if debug:
                print(f"Shortest Path Length: {nx.shortest_path_length(G, source=0, target=1)}")
            return G