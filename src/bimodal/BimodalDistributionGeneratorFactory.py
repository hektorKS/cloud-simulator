from src.bimodal.BimodalDistributionGenerator import BimodalDistributionGenerator

NUMBER_OF_ELEMENTS = 10000
STANDARD_DEVIATION = 60
MEAN1 = 2000


class BimodalDistributionGeneratorFactory:

    @staticmethod
    def create(coefficient_of_variation: float):
        return BimodalDistributionGenerator(
            NUMBER_OF_ELEMENTS,
            STANDARD_DEVIATION,
            coefficient_of_variation,
            MEAN1
        )
