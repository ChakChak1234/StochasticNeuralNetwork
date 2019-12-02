from pprint import pprint
from networks import BaseNetwork
from datetime import datetime
from network_algorithms import CreateSimpleRandomNetwork


def run_base_network_test(*args, **kwargs) -> dict:
    """

    :param args:
    :param kwargs:
    :return:
    """
    print(f"""
    
    Testing Base Network 
    Timestamp: {datetime.now()}
    
    """)

    network = BaseNetwork()
    CreateSimpleRandomNetwork(
        network=network,
        number_of_neurons=100,
        **kwargs
    )

    print(f"Nodes: {len(network.nodes())}")
    print(f"Edges: {len(network.edges())}")

    for _ in range(50):
        network.timestep(debug=True)
