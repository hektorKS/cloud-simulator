import random

import numpy as np

from src.bimodal.Generator import Generator

SEED_MIN_VALUE = 0
SEED_MAX_VALUE = 100000


class BimodalDistributionGenerator(Generator):

    def __init__(self, number_of_elements: int, space_between_peaks: int, standard_deviation: int,
                 percentage_of_short_elements: float, seed: int = None):
        Generator.__init__(self)
        assert number_of_elements > 0
        assert space_between_peaks > 0
        assert standard_deviation > 0
        assert percentage_of_short_elements >= 0.0
        assert percentage_of_short_elements <= 1.0
        self.number_of_elements = number_of_elements
        self.space_between_peaks = space_between_peaks
        self.standard_deviation = standard_deviation
        self.seed = seed
        self.percentage_of_short_elements = percentage_of_short_elements

    def generate(self):
        self.__reset_numpy_random_state()
        bimodal_distribution = np.concatenate((
            self.__generate_normal_distribution_of_half(int((self.number_of_elements - self.space_between_peaks) / 2),
                                                        self.percentage_of_short_elements),
            self.__generate_normal_distribution_of_half(int((self.number_of_elements + self.space_between_peaks) / 2),
                                                        1.0 - self.percentage_of_short_elements)
        ))
        return bimodal_distribution.astype(int)

    def __reset_numpy_random_state(self):
        if self.seed is None:
            seed = random.randint(SEED_MIN_VALUE, SEED_MAX_VALUE)
        else:
            seed = self.seed
        np.random.seed(seed)

    def __generate_normal_distribution_of_half(self, mean: int, percentage_of_elements: float):
        return np.random.normal(mean, self.standard_deviation, int(percentage_of_elements * self.number_of_elements))
