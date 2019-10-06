from src.bimodal.BimodalDistributionGenerator import BimodalDistributionGenerator
from src.bimodal.HistogramDrawer import HistogramDrawer

NUMBER_OF_HISTOGRAM_COLUMNS = 100

NUMBER_OF_ELEMENTS = 1000
SPACE_BETWEEN_PEAKS = 500
STANDARD_DEVIATION = 100
PERCENTAGE_OF_SHORT_ELEMENTS = 0.5


def main():
    bimodal_distribution_generator = BimodalDistributionGenerator(
        NUMBER_OF_ELEMENTS,
        SPACE_BETWEEN_PEAKS,
        STANDARD_DEVIATION,
        PERCENTAGE_OF_SHORT_ELEMENTS
    )
    bimodal_distribution = bimodal_distribution_generator.generate()
    HistogramDrawer.draw(bimodal_distribution, NUMBER_OF_HISTOGRAM_COLUMNS)


if __name__ == "__main__":
    main()
