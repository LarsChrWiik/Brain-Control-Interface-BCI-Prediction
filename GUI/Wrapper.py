
from BciObject import BciObject

class Wrapper:

    bciObject = BciObject()

    def train():
        return bciObject.train()


    def preprocess():
        return bciObject.preprocess()


    def predict():
        return bciObject.predict()
