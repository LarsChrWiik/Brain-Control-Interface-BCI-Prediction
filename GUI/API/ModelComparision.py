from sklearn.model_selection import cross_val_score
from sklearn.metrics import cohen_kappa_score, classification_report
from sklearn.model_selection import train_test_split

# TODO: cleaning.
class ModelComparision:


    def __init__(self, classifier, X, Y, test_size):
        # Divide into training and test set.
        training, testing_input, target, testing_target = train_test_split(
            X,
            Y,
            test_size=test_size
        )
        self.X = X
        self.Y = Y
        self.training_input = training
        self.testing_input = testing_input
        self.training_target = target
        self.testing_target = testing_target
        self.model = classifier
        self.true = 0
        self.false = 0

    def run(self):
        self.fit()
        prediciton = self.predict(self.testing_input)
        cv = self.cross_validation(5)
        report = self.report(prediciton, self.testing_target)
        print("Kappa " + str(self.kappa(prediciton)))
        print(report)
        print("Cross-Validation " + str(cv))
        print(self.get_ratio())


    def fit(self):
        self.model.fit(self.training_input, self.training_target)

    def predict(self, X):
        prediction = self.model.predict(X)
        for i in prediction:
            if i == 0:
                self.false +=1
            elif i == 1:
                self.true +=1
        return prediction

    def score(self):
        return self.model.score(self.X, self.Y)

    def cross_validation(self, k_folds):
        return cross_val_score(self.model, self.X, self.Y, cv=k_folds)

    def kappa(self, prediciton):
        return cohen_kappa_score(self.testing_target, prediciton)

    def report(self, target, predictions):
        return classification_report(target, predictions)

    def get_ratio(self):
        return "Class 0 / (Class 1 + Class 0) = " + str(self.false/(self.true + self.false))