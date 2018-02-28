
from API.PredictionModel import PredictionModel
from API.Preprocessor import Preprocessor

class BciObject:

    prediction_model = PredictionModel()
    preprocessor = Preprocessor()

    """
    This function is used fr development only. 
    """
    def development(self, data_raw):

        # Pre-process the data.
        X, Y = self.preprocessor.preprocess(data_raw)

        # Validate performance.
        self.prediction_model.cross_validation(X, Y)

    """
    Train the prediction model. 
    """
    def train(self, data_raw):
        print("Not implemented")

    """
    Make a prediction using the prediction model. 
    """
    def predict(self):
        print("Not implemented")

    """
    Extract statistics from the model building process. 
    """
    def get_statistics(self):
        print("Not implemented")