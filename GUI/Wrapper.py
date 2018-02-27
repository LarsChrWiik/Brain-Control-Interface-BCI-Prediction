
from API.BciObject import BciObject

class Wrapper:

    bciObject = BciObject()

    def train(self, data_raw):
        return self.bciObject.train(data_raw)

    """
    def preprocess(self):
        return self.bciObject.preprocess()
    """

    def predict(self):
        return self.bciObject.predict()
