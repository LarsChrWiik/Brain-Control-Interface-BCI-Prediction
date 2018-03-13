
from API.Model.PredictionModel import PredictionModel
from API.Preprocessing.Preprocessor import Preprocessor
from API.Model.ModelComparison import ModelComparison
from API.Randomizer import Randomizer


class BciObject:

    prediction_model = PredictionModel()
    preprocessor = Preprocessor()

    """
    Train the prediction model. 
    """
    def train(
            self,
            data_raw,
            shrink_percent=0,
            verbose=False
    ):
        self.clear_statistics()

        # Pre-process the data.
        X, Y = self.preprocessor.preprocess(
            data_raw=data_raw,
            with_targets=True,
            shrink_percent=shrink_percent,
            should_balance=True,
            verbose=verbose
        )

        # Randomize the data.
        X, Y = Randomizer.shuffle_two_lists(X, Y)

        # Train the prediction model.
        self.prediction_model.train(X, Y)

    """
    Make a prediction using the prediction model. 
    """
    def predict(self, data_raw, verbose=False):
        # Pre-process the data.
        X = self.preprocessor.preprocess(data_raw, with_targets=False, verbose=verbose)

        # Make prediction.
        prediction = self.prediction_model.predict(X)

        return prediction

    """
    Clear the statistical history. 
    """
    def clear_statistics(self):
        self.preprocessor.clear_statistics()
        self.prediction_model.clear_statistics()

    # TODO: Maybe move this function else-where.
    """
    Compare performance of different models. 
    """
    def compare_models(self, data_raw, verbose=False, shrink_percent=0):
        # Pre-process the data.
        X, Y = self.preprocessor.preprocess(data_raw, shrink_percent=shrink_percent, verbose=verbose)

        # Randomize the data.
        X, Y = Randomizer.shuffle_two_lists(X, Y)

        # Compare models.
        ModelComparison.start(X, Y)