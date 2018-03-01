
from API.PredictionModel import PredictionModel
from API.Preprocessor import Preprocessor
from API.ModelComparision import ModelComparision
from sklearn.metrics import recall_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import average_precision_score
from sklearn.metrics import cohen_kappa_score, classification_report

# TODO: Remove after ModelComparison has been implemented.
from sklearn.svm import SVC
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier


class BciObject:

    prediction_model = PredictionModel()
    preprocessor = Preprocessor()

    """
    This function is used fr development only. 
    """
    def development(self, data_raw):

        # Pre-process the data.
        X, Y = self.preprocessor.preprocess(data_raw, shrink_percent=0.7)

        # TODO: Temporary test.
        # Initialize predition model.
        clf = SVC()

        model = ModelComparision(clf, X, Y, test_size=0.3)
        model.run()


        # TODO:
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

    """
    Train the prediction model. 
    """
    def train(self, data_raw):
        X, Y = Preprocessor.preprocess(data_raw)
        self.prediction_model.fit(X, Y)

    """
    Make a prediction using the prediction model. 
    """
    def predict(self, data_raw):
        X = Preprocessor.preprocess(data_raw)
        self.prediction_model.predict(X)

    """
    Extract statistics from the model building process. 
    """
    def get_statistics(self):
        print("Not implemented")