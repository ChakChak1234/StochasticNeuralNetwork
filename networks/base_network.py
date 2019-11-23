import networkx as nx
from neurons import BaseNeuron
from structure_objects import EdgeWeight


class BaseNetwork(nx.DiGraph):
    """

    """
    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        super().__init__()

    def _serve_neuron_model(self, node_id) -> BaseNeuron:
        """

        :param node_id:
        :return:
        """
        return self.nodes[node_id]['model']

    def _serve_edge_weight(self, source, target) -> EdgeWeight:
        """

        :param source:
        :param target:
        :return:
        """
        return self[source][target]['weight']

    def timestep(self,
                 *args, **kwargs) -> dict:
        """

        :param args:
        :param kwargs:
        :return:
        """
        return_value = {}

        ActiveNeurons = []

        # Calculating Firing
        """
        
        
        """
        for node_id in self.nodes():
            model = self._serve_neuron_model(node_id=node_id)
            model_return = model.timestep()
            if model_return['fired']:
                ActiveNeurons.append(node_id)

        # Calculating Neuronal Communication
        for node_id in ActiveNeurons:
            for succ in self.successors(node_id):
                weight = self._serve_edge_weight(source=node_id, target=succ)
                receiver = self._serve_neuron_model(succ)
                receiver.update_input(
                    weight=weight
                )

        return return_value