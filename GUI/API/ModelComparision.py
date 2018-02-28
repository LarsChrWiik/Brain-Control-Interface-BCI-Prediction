from sklearn.model_selection import cross_val_score
from sklearn.metrics import cohen_kappa_score, classification_report


class ModelComparision:



    def __init__(self, classifier, training, target, testing_input, testing_target):
        self.model = classifier
        self.true = 0
        self.false = 0
        self.run(training, target, testing_input, testing_target)

    def run(self, training_input, training_target, testing_input, testing_target):
        self.fit(training_input, training_target)
        prediciton = self.predict(testing_input)
        self.report(prediciton, testing_target)


    def fit(self, X, Y):
        self.model.fit(X, Y)

    def predict(self, X):
        prediction =  self.model.predict(X)
        for i in prediction:
            if i == 0:
                self.false +=1
            elif i == 1:
                self.ture +=1
        return prediction

    def score(self, X, Y):
        return self.model.score(X, Y)

    def cross_validation(self, X, Y, k_folds):
        return cross_val_score(self.model, X, Y, cv=k_folds)

    def statistics(self, X, Y):
        return cohen_kappa_score(X, Y)

    def report(self, target, predictions):
        return self.model.classification_report(target, predictions)