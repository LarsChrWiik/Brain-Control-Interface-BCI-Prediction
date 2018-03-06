
from API.Model.PredictionModel import PredictionModel
from API.Preprocessing.Preprocessor import Preprocessor
from API.Model.ModelComparison import ModelComparison
from API.Randomizer import Randomizer


class BciObject:

    prediction_model = PredictionModel()

    """
    Train the prediction model. 
    """
    def train(
            self, data_raw,
            with_targets=True,
            shrink_percent=0,
            should_balance=True
    ):
        # Pre-process the data.
        X, Y = Preprocessor.preprocess(
            data_raw,
            with_targets,
            shrink_percent,
            should_balance
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
        X = Preprocessor.preprocess(data_raw)

        # Make prediction.
        prediction = self.prediction_model.predict(X)

        return prediction

    """
    Extract statistics from the model building process. 
    """
    def get_statistics(self):
        print("Not implemented")
        pass

    # TODO: Maybe move this function else-where.
    """
    Compare performance of different models. 
    """
    def compare_models(self, data_raw):
        # Pre-process the data.
        X, Y = Preprocessor.preprocess(
            data_raw,
            shrink_percent=0.7
        )

        # Randomize the data.
        X, Y = Randomizer.shuffle_two_lists(X, Y)

        # Compare models.
        ModelComparison.start(X, Y)