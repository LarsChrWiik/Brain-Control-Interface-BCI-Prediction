
from sklearn.model_selection import train_test_split
from API.Statistics.PredictionModelStatistics import PredictionModelStatistics
from sklearn.model_selection import cross_val_score

from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier, VotingClassifier


class PredictionModel:

    def __init__(self):
        self.model_statistics = PredictionModelStatistics()
        self.classifiers = [ ("SVC", SVC()),
                             ("KNN", KNeighborsClassifier(n_neighbors=9)),
                             ("GBC",GradientBoostingClassifier(max_depth=5)),
                             ("MLP", MLPClassifier(activation="tanh"))
                             ]
        self.classifier = VotingClassifier(estimators = self.classifiers,)

    def train(self, X, Y, test_size=0.3, k_fold=10):
        # split for validation
        training_input, testing_input, training_target, testing_target = train_test_split(
            X,
            Y,
            test_size=test_size
        )

        # Train
        self.classifier.fit(training_input,testing_target)

        # Validate
        prediction = self.classifier.predict(testing_input)

        # Add statistics
        self.model_statistics.fill(testing_target, prediction)

    def predict(self, X):
        return self.classifier.predict(X)


    def clear_statistics(self):
        self.model_statistics.clear_statistics()
