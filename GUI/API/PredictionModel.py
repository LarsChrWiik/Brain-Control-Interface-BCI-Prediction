from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

# Prediction model.
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
        ans = [a ,b, c]
        return ans

    # TODO: Cross validaiton.

    # Validation Method
    def validation(self):
        print("Not implemented")

    # Prediction Method
    def predict(self):
        print("Not implemented")

"""

from sklearn.model_selection import KFold


# Apply k-fold cross validation and return the score.
def cross_validate(classifier, data, n_split, verbose = False):
    kf = KFold(n_splits=n_split)
    sum = 0.0
    counter = 0
    for train, test in kf.split(data):
        if verbose:
            print(str(round(counter * 100 / n_split, 3)) + "%")
            counter += 1
        train_set = np.array(data)[train]
        test_set = np.array(data)[test]
        clf = classifier.train(train_set)
        sum += accuracy(clf, test_set)
    if verbose:
        print(str(round(counter * 100 / n_split, 1)) + "%")
    return round(sum / n_split, 5)

"""

