from pprint import pprint

from neurons import BaseNeuron



def run_base_neuron_test(*args, **kwargs) -> dict:
    """

    :param args:
    :param kwargs:
    :return:
    """
    print("Testing Base Neuron")
    neuron = BaseNeuron()

    print("Running Timestep")
    for _ in range(100):
        return_value = neuron.timestep()
        pprint(return_value)
