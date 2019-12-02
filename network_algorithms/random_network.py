from networks import BaseNetwork
from neurons import BaseNeuron
from structure_objects import EdgeWeight
from random import random


def CreateSimpleRandomNetwork(network: BaseNetwork=None,
                              number_of_neurons: int=1000,
                              proportion_excitatory: float=0.8,
                              p_e2e: float=0.3,
                              p_e2i: float=0.3,
                              p_i2i: float=0.1,
                              p_i2e: float=0.4,
                              w_e_min: float=0.0,
                              w_e_max: float=10.0,
                              w_i_min: float=0.0,
                              w_i_max: float=15.0,
                              *args, **kwargs):
    """

    :param network:
    :param number_of_neurons:
    :param proportion_excitatory:
    :param p_e2e:
    :param p_e2i:
    :param p_i2i:
    :param p_i2e:
    :param w_e_min:
    :param w_e_max:
    :param w_i_min:
    :param w_i_max:
    :param args:
    :param kwargs:
    :return:
    """
    if network is None:
        network = BaseNetwork()

    network.add_nodes_from(range(number_of_neurons))
    number_of_excitatory = int(proportion_excitatory * number_of_neurons)
    number_of_inhibitory = number_of_neurons - number_of_excitatory
    neurons = [node for node in network.nodes()]
    excitatory_neurons = tuple(neurons[:number_of_excitatory])
    inhibitory_neurons = tuple(neurons[number_of_excitatory:])
    probability_breakdown = {
        excitatory_neurons: {
            excitatory_neurons: p_e2e,
            inhibitory_neurons: p_e2i
        },
        inhibitory_neurons: {
            excitatory_neurons: p_i2e,
            inhibitory_neurons: p_i2i
        }
    }

    for source in probability_breakdown:
        for s in source:
            network.nodes[s]['model'] = BaseNeuron()

        for target in probability_breakdown[source]:
            p = probability_breakdown[source][target]
            for s in source:
                for t in target:
                    if random() < p:
                        if source is excitatory_neurons:
                            w = (w_e_max - w_e_min) * random() + w_e_min
                        elif source is inhibitory_neurons:
                            w = -((w_i_max - w_i_min) * random() + w_i_min)
                        network.add_edge(
                            u_of_edge=s,
                            v_of_edge=t,
                            weight=EdgeWeight(
                                _weight=w
                            )
                        )

    return network