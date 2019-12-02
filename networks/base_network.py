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
        self.current_timestep = 0

    def add_neuron_model(self, neuron):
        """

        :param neuron:
        :return:
        """

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
                 debug: bool=False,
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

        if debug:
            print(f"{self.current_timestep}|Active Neurons: {len(ActiveNeurons)}")

        # Calculating Neuronal Communication
        for node_id in ActiveNeurons:
            for succ in self.successors(node_id):
                weight = self._serve_edge_weight(source=node_id, target=succ)
                receiver = self._serve_neuron_model(succ)
                receiver.update_input(
                    weight=weight
                )

        self.current_timestep += 1

        return return_value


if __name__ == "__main__":
    from datetime import datetime
    print(f"""
    
    Running Network 
    
    """)