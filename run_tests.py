from neurons.test_scripts import run_base_neuron_test
from networks.test_scripts import run_base_network_test
from network_algorithms.test_scripts import run_shortest_path_generation_test


tests = {
    "BaseNeuron": run_base_neuron_test,
    "BaseNetwork": run_base_network_test,
    "BaseNetworkGeneration": run_shortest_path_generation_test
}

def run_test(test_type: str,
             *args, **kwargs):
    """

    :param test_type:
    :param args:
    :param kwargs:
    :return:
    """
    if test_type not in tests:
        raise Exception

    test = tests[test_type]
    test()
