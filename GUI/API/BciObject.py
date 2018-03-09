
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
            with_targets=True,
            shrink_percent=0,
            should_balance=True,
            verbose=False
    ):
        self.clear_statistics()

        # Pre-process the data.
        X, Y = self.preprocessor.preprocess(
            data_raw,
            with_targets,
            shrink_percent,
            should_balance,
            verbose
        )

        # Randomize the data.
        X, Y = Randomizer.shuffle_two_lists(X, Y)

        # Train the prediction model.
        self.prediction_model.fit(X, Y)

    """
    Make a prediction using the prediction model. 
    """
    def predict(self, data_raw):
        # Pre-process the data.
        X = self.preprocessor.preprocess(data_raw)

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
    def compare_models(self, data_raw, verbose=False):
        # Pre-process the data.
        X, Y = self.preprocessor.preprocess(data_raw, verbose=verbose)

        # Randomize the data.
        X, Y = Randomizer.shuffle_two_lists(X, Y)

        # Compare models.
        ModelComparison.start(X, Y)