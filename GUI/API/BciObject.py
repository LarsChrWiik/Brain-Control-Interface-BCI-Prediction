
from API.PredictionModel import PredictionModel
from API.Preprocessor import Preprocessor

class BciObject:

    prediction_model = PredictionModel()
    preprocessor = Preprocessor()

    """
    This function is used fr development only. 
    """
    def development(self, data_raw, train_size=None):

        # Pre-process the data.
        X, Y = self.preprocessor.preprocess(data_raw)

        # Validate performane.
        self.prediction_model.cross_validation(X, Y)

    def train(self, data_raw):
        print("Not implemented")

    def predict(self):
        print("Not implemented")

    def get_statistics(self):
        print("Not implemented")