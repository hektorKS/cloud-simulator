from src.bimodal.BimodalDistributionGenerator import BimodalDistributionGenerator

NUMBER_OF_ELEMENTS = 10000
STANDARD_DEVIATION = 60


class BimodalDistributionGeneratorFactory:

    @staticmethod
    def create(coefficient_of_variation: float, mean1: int):
        return BimodalDistributionGenerator(
            NUMBER_OF_ELEMENTS,
            STANDARD_DEVIATION,
            coefficient_of_variation,
            mean1
        )
