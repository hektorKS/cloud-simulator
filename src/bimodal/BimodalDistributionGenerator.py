import random

import numpy as np

SEED_MIN_VALUE = 0
SEED_MAX_VALUE = 100000


class BimodalDistributionGenerator:

    def __init__(self, number_of_elements: int, space_between_peaks: int, standard_deviation: int, seed: int = None):
        assert number_of_elements > 0
        assert space_between_peaks > 0
        assert standard_deviation > 0
        self.number_of_elements = number_of_elements
        self.space_between_peaks = space_between_peaks
        self.standard_deviation = standard_deviation
        self.seed = seed

    def generate(self):
        self.__reset_numpy_random_state()
        bimodal_distribution = np.concatenate((
            self.__generate_normal_distribution_of_half(int((self.number_of_elements - self.space_between_peaks) / 2)),
            self.__generate_normal_distribution_of_half(int((self.number_of_elements + self.space_between_peaks) / 2))
        ))
        return bimodal_distribution.astype(int)

    def __reset_numpy_random_state(self):
        if self.seed is None:
            self.seed = random.randint(SEED_MIN_VALUE, SEED_MAX_VALUE)
        np.random.seed(self.seed)

    def __generate_normal_distribution_of_half(self, mean: int):
        return np.random.normal(mean, self.standard_deviation, int(0.5 * self.number_of_elements))

