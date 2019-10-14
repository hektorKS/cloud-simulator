from src.bimodal.BimodalDistributionGenerator import BimodalDistributionGenerator
from src.bimodal.HistogramDrawer import HistogramDrawer


def main():
    bimodal_distribution_generator = BimodalDistributionGenerator(coefficient=10)
    bimodal_distribution = bimodal_distribution_generator.generate()
    HistogramDrawer.draw(bimodal_distribution)


if __name__ == "__main__":
    main()
