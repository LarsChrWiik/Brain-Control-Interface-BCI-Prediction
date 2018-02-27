
import matplotlib.pyplot as plt

# TODO: This file should be removed, its only for development.
"""
Class used for debugging, interpretation and debugging. 
"""
class Visualization:

    @staticmethod
    def visualize_1(singals, flashing):
        singal = []
        for ts in singals:
            singal.append(ts[0])

        # Visualize.
        graph = plt.plot(singal)
        plt.show()

    @staticmethod
    def visualize_2(stimulus_type):
        # Visualize
        graph = plt.plot(stimulus_type)
        plt.show()

