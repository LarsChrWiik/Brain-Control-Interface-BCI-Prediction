
from BciObject import BciObject

class Wrapper:

    bciObject = BciObject()

    def train(self):
        return self.bciObject.train()


    def preprocess(self):
        return self.bciObject.preprocess()


    def predict(self):
        return self.bciObject.predict()
