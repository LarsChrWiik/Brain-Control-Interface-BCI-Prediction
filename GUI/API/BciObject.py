
from API.Model.PredictionModel import PredictionModel
from API.Preprocessing.Preprocessor import Preprocessor
from API.Model.ModelBenchmark import ModelBenchmark
from API.Randomizer import Randomizer

# TODO: Remove after ModelComparison has been implemented.
from sklearn.svm import SVC


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

    # TODO: This function is only for development.
    # TODO: (Remove when project is finished).
    """
    This function is used fr development only. 
    """
    def development(self, data_raw):
        # Pre-process the data.
        X, Y = Preprocessor.preprocess(
            data_raw,
            shrink_percent=0.7
        )

        # Initialize predition model.
        clf = SVC()

        model = ModelBenchmark(clf, X, Y, test_size=0.3)
        model.run()

        # TODO: fix.
        """
        # Validate performance.
        score = cross_val_score(clf, X, Y, cv=3)
        print("Cross_val = " + str(score))

        # Fit the model.
        clf.fit(X_train, y_train)

        # Predict test set.
        predictions = clf.predict(X_test)

        print("predictions = " + str(predictions))

        # Precision.
        print("Precision = " + str(average_precision_score(y_test, predictions)))

        # Recall.
        print("Recall = " + str(recall_score(y_test, predictions)))
        """