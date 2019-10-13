from src.bimodal.BimodalDistributionGeneratorFactory import BimodalDistributionGeneratorFactory
from src.bimodal.HistogramDrawer import HistogramDrawer

COEFFICIENT_OF_VARIATION = 10
MEAN1 = 300


def main():
    bimodal_distribution_generator = BimodalDistributionGeneratorFactory.create(
        COEFFICIENT_OF_VARIATION,
        MEAN1
    )
    bimodal_distribution = bimodal_distribution_generator.generate()
    HistogramDrawer.draw(bimodal_distribution)
    print("Coefficient of variation {}".format(round(bimodal_distribution.std() / bimodal_distribution.mean(), 3)))


if __name__ == "__main__":
    main()
