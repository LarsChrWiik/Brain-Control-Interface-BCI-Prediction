
from API.Model.ModelBenchmark import ModelBenchmark
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB ,BernoulliNB
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier

"""
Class used for comparing different models.
"""
class ModelComparison:

    @staticmethod
    def start(X, Y):

        # Support Vector Machine.
        ModelBenchmark.run(SVC(), X, Y)

        # 3-Nearest Neighbor.
        ModelBenchmark.run(
            KNeighborsClassifier(n_neighbors=3),
            X,
            Y
        )

        # 5-Nearest Neighbor.
        ModelBenchmark.run(
            KNeighborsClassifier(n_neighbors=5),
            X,
            Y
        )
        # 7-Nearest Neighbor.
        ModelBenchmark.run(
            KNeighborsClassifier(n_neighbors=7),
            X,
            Y
        )

        # Naive Bayes classifier for multinomial models.
        ModelBenchmark.run(MultinomialNB(), X, Y)

        # Naive Bayes classifier for multivariate Bernoulli models.
        ModelBenchmark.run(BernoulliNB(), X, Y)

        # Gaussian Naive Bayes
        ModelBenchmark.run(GaussianNB(), X, Y)

        # Gradient Boosting
        ModelBenchmark.run(GradientBoostingClassifier(), X, Y)

        # MLP
        ModelBenchmark.run(MLPClassifier(), X, Y)

        # Stochastic Gradient Descent
        ModelBenchmark.run(SGDClassifier(shuffle=True), X, Y)

        # Decision Tree Classifer
        ModelBenchmark.run(DecisionTreeClassifier(), X, Y)
