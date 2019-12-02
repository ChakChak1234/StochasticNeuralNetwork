import networkx as nx
from networks import BaseNetwork


def generate_network_structure(graph: nx.Graph,
                               source: int=0,
                               target: int=1,
                               *args, **kwargs) -> BaseNetwork:
    """

    :param graph:
    :param args:
    :param kwargs:
    :return:
    """
    network = BaseNetwork()

    # Add Source and Target Components

    # Create Components
