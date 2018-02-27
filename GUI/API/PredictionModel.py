from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression

# Prediction model.
class PredictionModel:
    """
    All of the models have been setup, but they may need some parameters changed.
    """

    """ Testing Data Structures """
    test_stimulus_code = []
    test_signal = []
    test_flashing = []

    """ Training Data Structures """
    training_stimulas_code = []
    training_stimulas_type = []
    training_target = []
    training_signal = []
    training_flashing = []

    """ Set up the classification models """
    # Svm
    model_one = svm.SVC()

    # Gaussian Naive Bayes
    model_two = GaussianNB()

    # Gradient Boosting
    modelThree = GradientBoostingClassifier()

    # Logistic Regression.
    clf_lg = LogisticRegression()

    """ 
    These two are a tad different, they are not models as such and will need looking into.
    That's if we don't just bin them off. 
    """

    # Logistic Regression

    # Lda

    # Training Method
    def train(self, X, Y):
        self.clf_lg.fit(X, Y)
        print("Not implemented")

    # Validation Method
    def validation(self):
        print("Not implemented")

    # Prediction Method
    def predict(self):
        print("Not implemented")
