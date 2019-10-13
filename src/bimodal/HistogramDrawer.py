import matplotlib.pyplot as plt
import numpy as np

NUMBER_OF_HISTOGRAM_COLUMNS = 100


class HistogramDrawer:

    @staticmethod
    def draw(elements: np.ndarray, number_of_histogram_columns: int = NUMBER_OF_HISTOGRAM_COLUMNS):
        plt.hist(elements, number_of_histogram_columns)
        plt.show()
