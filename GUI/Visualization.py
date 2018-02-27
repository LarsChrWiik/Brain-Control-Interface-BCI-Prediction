
import matplotlib.pyplot as plt

class Visualization:

    # Used for testing.
    @staticmethod
    def visualize_1(singals, flashing):
        singal = []
        for ts in singals:
            singal.append(ts[0])

        # Visualize.
        print(flashing)
        # Plot.
        graph = plt.plot(singal)
        # Legend.
        plt.show()

