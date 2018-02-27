
from Importer import Importer
from Wrapper import Wrapper
from Visualization import Visualization

filename_trian_A = "Subject_A_Train.mat"
filename_test_A = "Subject_A_Test.mat"

wrapper = Wrapper()

def train():
    # Import mat file.
    data_raw = Importer.mat(filename_trian_A)

    Visualization.visualize_1(
        data_raw["Signal"][4],
        data_raw["Flashing"][0],
    )

    #wrapper.train(data_raw)

train()

