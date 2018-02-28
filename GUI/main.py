
from Importer import Importer
from Wrapper import Wrapper
from Visualization import Visualization

filename_train_A = "Subject_A_Train.mat"
filename_test_A = "Subject_A_Test.mat"

wrapper = Wrapper()

# TODO: This should be triggered through the user interface GUI.
# Train the bci-classifier using input file.
def train(filename):
    # Import mat file.
    data_raw = Importer.mat(filename)

    # Make data_raw smaller.
    for row in data_raw:
        data_raw[row] = data_raw[row][:1]

    # Train.
    wrapper.train(data_raw)


train(filename_train_A)

