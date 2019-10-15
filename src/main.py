from src.bimodal.BimodalDistributionGenerator import BimodalDistributionGenerator
from src.bimodal.HistogramDrawer import HistogramDrawer
import numpy as np


def main():
    bimodal_distribution_generator = BimodalDistributionGenerator(coefficient=10)
    bimodal_distribution = bimodal_distribution_generator.generate()
    HistogramDrawer.draw(bimodal_distribution)
    print(f'mean: {np.mean(bimodal_distribution)}')
    print(f'std: {np.std(bimodal_distribution)}')
    print(f'coeff: {np.std(bimodal_distribution)  / np.mean(bimodal_distribution)}')


if __name__ == "__main__":
    main()
