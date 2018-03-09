
from API.BciObject import BciObject

"""
This class is used as wrapper/bridge between the GUI and the API.
The wrapper only contain 1 instance of a BCI-object. 
"""
class Wrapper:

    bciObject = BciObject()

    # TODO: FOR DEVELOPMENT:
    def compare_models(self, data_raw):
        return self.bciObject.compare_models(data_raw)

    def train(self, data_raw, with_targets=True, shrink_percent=0, should_balance=True, verbose=False):
        return self.bciObject.train(data_raw)

    def predict(self, data_raw):
        return self.bciObject.predict(data_raw)
