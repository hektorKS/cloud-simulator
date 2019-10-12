from src.bimodal.BimodalDistributionGenerator import BimodalDistributionGenerator
from src.bimodal.HistogramDrawer import HistogramDrawer


NUMBER_OF_HISTOGRAM_COLUMNS = 100

NUMBER_OF_ELEMENTS = 10000
STANDARD_DEVIATION = 60
COEFFICIENT_OF_VARIATION = 10
MEAN1 = 300


def main():
    bimodal_distribution_generator = BimodalDistributionGenerator(
        NUMBER_OF_ELEMENTS,
        STANDARD_DEVIATION,
        COEFFICIENT_OF_VARIATION,
        MEAN1
    )
    bimodal_distribution = bimodal_distribution_generator.generate()
    HistogramDrawer.draw(bimodal_distribution, NUMBER_OF_HISTOGRAM_COLUMNS)
    print("coefficient of variation {}".format(round(bimodal_distribution.std() / bimodal_distribution.mean(), 3)))


if __name__ == "__main__":
    main()
