
import matplotlib.pyplot as plt
import numpy as np

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

    #todo - check the function inputs as definitions needs data its not getting
    #     #@staticmethod
    # def channelGraph(channelData):
    #     ##Graph - This belongs somewhere else probably.
    #     t = np.linspace(0, len(channelData), len(channelData), endpoint=False)
    #     plt.plot(t, y)
    #     plt.grid(True)
    #     plt.axis('tight')
    #     tick = np.linspace(0, len(data), len(data) / samplingFreq)
    #     plt.xticks(tick, range(lengthOfTestSeconds)) ##32 seconds per test?
    #     plt.xlabel("Time in Seconds")
    #     plt.legend(loc='upper left')
    #     plt.show()

