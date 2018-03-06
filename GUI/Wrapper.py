
from API.BciObject import BciObject

"""
This class is used as wrapper/bridge between the GUI and the API.
The wrapper only contain 1 instance of a BCI-object. 
"""
class Wrapper:

    bciObject = BciObject()

    # TODO: FOR DEVELOPMENT:
    def development(self, data_raw):
        return self.bciObject.compare_models(data_raw)

    def train(self, data_raw):
        return self.bciObject.train(data_raw)

    def predict(self):
        return self.bciObject.predict()
