import random
from math import sqrt

import numpy as np

from src.bimodal.DistributionGenerator import DistributionGenerator

SEED_MIN_VALUE = 0
SEED_MAX_VALUE = 100000


class BimodalDistributionGenerator(DistributionGenerator):

    def __init__(self, number_of_elements: int, standard_deviation: int,
                 coefficient_of_variation: float, mean1: int, seed: int = None):
        DistributionGenerator.__init__(self)
        assert number_of_elements > 0
        assert standard_deviation > 0
        self.number_of_elements = number_of_elements
        self.standard_deviation = standard_deviation
        self.seed = seed
        self.coefficient_of_variation = coefficient_of_variation
        self.percentage_of_short_elements = self.__calculate_percentage_of_short_elements()
        self.mean1 = mean1
        self.mean2 = self.__calculate_mean2()

    def generate(self):
        self.__reset_numpy_random_state()
        bimodal_distribution = np.concatenate((
            self.__generate_normal_distribution_of_half(int(self.mean1), self.percentage_of_short_elements),
            self.__generate_normal_distribution_of_half(int(self.mean2), 1.0 - self.percentage_of_short_elements)
        ))

        assert bimodal_distribution[bimodal_distribution <= 0].size <= 0, \
            "Bad params passed to generator, negative value occurred"
        return bimodal_distribution.astype(int)

    def __reset_numpy_random_state(self):
        if self.seed is None:
            seed = random.randint(SEED_MIN_VALUE, SEED_MAX_VALUE)
        else:
            seed = self.seed
        np.random.seed(seed)

    def __generate_normal_distribution_of_half(self, mean: int, percentage_of_elements: float):
        return np.random.normal(mean, self.standard_deviation, int(percentage_of_elements * self.number_of_elements))

    def __calculate_percentage_of_short_elements(self):
        x = self.coefficient_of_variation
        if x >= 1.2:
            return max(pow(x, 2) / (pow(x, 2) + 1) + 0.005, 0.75)
        else:
            return 0.5 + 0.25 * self.coefficient_of_variation

    def __calculate_mean2(self):
        p = self.percentage_of_short_elements
        x = self.coefficient_of_variation
        m = self.mean1
        return (p * (pow(x, 2) + 1) * (sqrt(-(p * pow(m, 2) * pow(x, 2)) / ((p - 1) * pow((p * pow(x, 2) + p - pow(x, 2)), 2))) + m) - pow(x,2) * sqrt(-(p * pow(m, 2) * pow(x, 2)) / ((p - 1) * pow((p * pow(x, 2) + p - pow(x, 2)), 2)))) / (p * pow(x, 2) + p - pow(x, 2))

    def set_number_of_elements(self, number_of_elements: int):
        self.number_of_elements = number_of_elements
