
from sklearn.model_selection import train_test_split
from API.Statistics.PredictionModelStatistics import PredictionModelStatistics
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

class PredictionModel:

    def __init__(self):
        self.model_statistics = PredictionModelStatistics()
        self.classifier = KNeighborsClassifier(n_neighbors=9)

    def train(self, X, Y, k_fold=10):

        # cross validate
        kf = KFold(n_splits=k_fold)
        for train, test in kf.split(X):
            # split data
            train_set = np.array(X)[train]
            train_set_ans = np.array(Y)[train]
            test_set = np.array(X)[test]
            test_set_ans = np.array(Y)[test]
            # train
            self.classifier.fit(train_set, train_set_ans)
            # predict
            prediction = np.array(self.classifier.predict(test_set))
            # update stats
            self.model_statistics.update(test_set_ans, prediction)

        # finish stats
        self.model_statistics.finish(k_fold)
        # Train
        self.classifier.fit(X, Y)



    def predict(self, X):
        return self.classifier.predict(X)


    def clear_statistics(self):
        self.model_statistics.clear_statistics()
