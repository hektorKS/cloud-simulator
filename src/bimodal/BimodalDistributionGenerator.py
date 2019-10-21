import random

import numpy as np

from src.bimodal.Generator import Generator

SEED_MIN_VALUE = 0
SEED_MAX_VALUE = 100000


class BimodalDistributionGenerator(Generator):

    def __init__(self,
                 coefficient: int,
                 n_elements: int = 10000,
                 first_mean: int = 0,
                 first_scale: float = 1.0,
                 second_mean: int = 100,
                 second_scale: float = 1.0,
                 seed: int = None):
        Generator.__init__(self)
        self.coefficient = coefficient
        self.n_elements = n_elements
        self.first_mean = first_mean
        self.first_scale = first_scale
        self.second_mean = second_mean
        self.second_scale = second_scale
        self.seed = seed

    def generate(self):

        expected_value = (self.first_scale * self.first_mean + self.second_scale * self.second_mean) / 2
        std = self.coefficient * expected_value
        print(f'Prior: expected value {expected_value}, std {std}')

        self.__reset_numpy_random_state()
        norm1 = self.__generate_normal_distribution_of_half(self.first_mean, std, self.first_scale)

        self.__reset_numpy_random_state()
        norm2 = self.__generate_normal_distribution_of_half(self.second_mean, std, self.second_scale)
        bimodal_distribution = np.concatenate((norm1, norm2))

        return bimodal_distribution

    def __reset_numpy_random_state(self):
        if self.seed is None:
            seed = random.randint(SEED_MIN_VALUE, SEED_MAX_VALUE)
        else:
            seed = self.seed

        np.random.seed(seed)

    def __generate_normal_distribution_of_half(self, mean: int, std: float, scale: float):
        return scale * np.random.normal(loc=mean, scale=std, size=self.n_elements)
