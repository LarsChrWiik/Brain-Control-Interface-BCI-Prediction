
from API.BciObject import BciObject

"""
This class is used as wrapper/bridge between the GUI and the API.
The wrapper only contain 1 instance of a BCI-object. 
"""
class Wrapper:

    bciObject = BciObject()

    # TODO: FOR DEVELOPMENT:
    def compare_models(self, data_raw, shrink_percent=0, verbose=False):
        return self.bciObject.compare_models(
            data_raw,
            shrink_percent=shrink_percent,
            verbose=verbose
        )

    def train(self, data_raw, shrink_percent=0, verbose=False):

        #TODO: remove (only for testing).
        # Make data_raw smaller.
        for row in data_raw:
            data_raw[row] = data_raw[row][:1]

        self.bciObject.train(
            data_raw=data_raw,
            shrink_percent=shrink_percent,
            verbose=verbose
        )

    def predict(self, data_raw, verbose=False):
        return self.bciObject.predict(data_raw, verbose=verbose)
