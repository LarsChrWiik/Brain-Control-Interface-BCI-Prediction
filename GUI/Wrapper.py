
from API.BciObject import BciObject

# Wrapper class for the GUI.
# This class is used as the bridge between the GUI and the API.
class Wrapper:

    bciObject = BciObject()

    # Train a prediction model using raw data.
    def train(self, data_raw):
        return self.bciObject.train(data_raw)

    def predict(self):
        return self.bciObject.predict()
