from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score


X, Y, classifier
"""
Ensemble model. 
This is build by several models. 
"""
class PredictionModel:

    """ Set up the classification models """


    # Svm
    model_one = SVC()

    # Gaussian Naive Bayes
    model_two = GaussianNB()

    # Gradient Boosting
    model_three = GradientBoostingClassifier()

    # Final classifier.
    #MLP = MLPClassifier()

    # Logistic Regression

    # Lda

    # Training Method



    def fit(self, X, Y):

        pass

    def score(self, X, Y):
        pass

    def predict(self, X):
        pass



"""
    def train(self, X, Y):
        # X input, Y target
        print("Model One Training")
        self.model_one.fit(X, Y)
        print("Model Two Training")
        self.model_two.fit(X, Y)
        print("Model Three Training")
        self.model_three.fit(X, Y)
    #   print("MLP Training")
    #   self.MLP.fit(X, Y)


    def score(self, X, Y):
        # X input, Y target
        a = self.model_one.score(X, Y)
        b = self.model_two.score(X, Y)
        c = self.model_three.score(X, Y)
        ans = [a, b, c]
        return ans


    def cross_validate(self, X, Y, k_folds = None):
        print("Cross-validaion begun 1")
        a = cross_val_score(self.model_one, X, Y, cv = k_folds)
        print("Cross-validaion begun 2")
        b = cross_val_score(self.model_two, X, Y, cv = k_folds)
        print("Cross-validaion begun 3")
        c = cross_val_score(self.model_three, X, Y, cv = k_folds)
        return [a, b, c]

"""
