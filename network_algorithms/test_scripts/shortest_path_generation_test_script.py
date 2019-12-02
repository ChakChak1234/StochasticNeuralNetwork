from network_algorithms.shortest_path_utils import create_base_random_graph
from datetime import datetime


def run_shortest_path_generation_test(*args, **kwargs):
    """

    :param args:
    :param kwargs:
    :return:
    """
    print(f"""
    
    Running Shortest Path Generation Test
    Timestamp: {datetime.now()}
    
    """)


    G = create_base_random_graph(debug=True)

    print(f"Nodes: {len(G.nodes())}")
    print(f"Edges: {len(G.edges())}")
