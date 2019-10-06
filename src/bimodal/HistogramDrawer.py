import matplotlib.pyplot as plt
import numpy as np


class HistogramDrawer:

    @staticmethod
    def draw(elements: np.ndarray, number_of_histogram_columns):
        plt.hist(elements, number_of_histogram_columns)
        plt.show()
