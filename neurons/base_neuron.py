from random import random
from math import exp, inf
from structure_objects import EdgeWeight


class BaseNeuron:
    """
    Setting up a basic Stochastic Neuron

    """
    def __init__(self,
                 _b: float=0.0,
                 _v: float=0.0,
                 _I: float=0.0,
                 _tau: int=10,
                 _active: bool=False,
                 _current_timestep: int=0,
                 _current_threshold: float=0.0,
                 *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        # Model Parameters
        self.b = _b
        self.v = _v
        self.I = _I
        self.tau = _tau

        # Pacing Parameters
        self.current_timestep = _current_timestep
        self.active = _active
        self.last_fired = -inf
        self.current_threshold = _current_threshold

    def set_parameters(self,
                       _b: float=0.0,
                       _v: float=0.0,
                       _I: float=0.0,
                       _tau: int=5,
                       *args, **kwargs):
        """

        :param _b:
        :param _v:
        :param _I:
        :param _tau:
        :param args:
        :param kwargs:
        :return:
        """
        self.b = _b
        self.v = _v
        self.I = _I
        self.tau = _tau

    def _reset_input(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        self.I = 0.0

    def update_input(self,
                     weight: EdgeWeight,
                     *args, **kwargs):
        """

        :param _I:
        :param args:
        :param kwargs:
        :return:
        """
        _I = weight.serve_weight()
        self.I += _I

    def _calculate_threshold_value(self):
        """

        :return:
        """
        self.current_threshold = exp(self.b + self.I) / self.tau

    def _reset_fired(self):
        """

        :return:
        """
        if self.current_timestep - self.last_fired > self.tau:
            self.active = False

    def _calculate_firing(self,
                          debug:bool=False,
                          *args, **kwargs):
        """

        :param args:
        :param kwargs:
        :return:
        """
        if random() < self.current_threshold:
            self.active = True
            self.last_fired = self.current_timestep
            if debug:
                print(f"Fired at {self.current_timestep}")

    def timestep(self,
                 debug: bool=False,
                 *args, **kwargs) -> dict:
        """

        :param args:
        :param kwargs:
        :return:
        """
        timestep_data = {}
        # Reset Fired
        self._reset_fired()

        if self.active:
            timestep_data['fired'] = False
            timestep_data['active'] = self.active
            self.current_timestep += 1
            return timestep_data

        self._calculate_threshold_value()

        self._calculate_firing(debug=debug)

        # Reset Inputs
        self._reset_input()
        self.current_timestep += 1

        timestep_data['fired'] = self.active
        timestep_data['active'] = self.active

        return timestep_data


if __name__ == "__main__":
    """
    
    """
    from datetime import datetime
    print(f"""
    Running Test of Neuron Base Class
    Time: {datetime.now()}
    """)
    neuron = BaseNeuron()
    neural_history = []
    milliseconds = 1000
    for idx in range(milliseconds):
        data = neuron.timestep(debug=True)
        if data['fired']:
            neural_history.append(idx)

    print(f"""
    
    Neural Firing Rate: {1000 * len(neural_history) / milliseconds} / Second
    
    """)
