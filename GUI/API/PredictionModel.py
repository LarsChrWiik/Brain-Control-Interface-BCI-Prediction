from sklearn import svm
from sklearn.naive_bayes import GaussianNB


# Prediction model.
class PredictionModel:

    """ SVM, LDA, Gaussian Naive Bayes, Gradient Boosting, Logistic Regression, """

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

    # LDA

    # Gaussian Naive Bayes
    model_two = GaussianNB()

    # Gradient Boosting


    # Logistic Regression


    # Training Method
    def train(self):
        print("Not implemented")

    # Validation Method
    def validation(self):
        print("Not implemented")

    # Prediction Method
    def predict(self):
        print("Not implemented")
