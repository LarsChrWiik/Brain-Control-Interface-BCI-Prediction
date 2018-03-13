
from API.Model.ModelBenchmark import ModelBenchmark
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier, VotingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
"""
Class used for comparing different models.
"""
class ModelComparison:

    @staticmethod
    def start(X, Y, verbose=True):
        if verbose: print("Started ModelComparison")

        # DummyClassifier
        ModelBenchmark.run(DummyClassifier(), X, Y)
        
        # LogisticRegression
        ModelBenchmark.run(LogisticRegression(solver="lbfgs", multi_class="multinomial"), X, Y)

        # Support Vector Machine.
        ModelBenchmark.run(SVC(), X, Y, custom_print="Default")

        # Support Vector Machine.
        ModelBenchmark.run(SVC(kernel="linear"), X, Y, custom_print="kernel=linear")

        # Support Vector Machine.
        ModelBenchmark.run(SVC(kernel="poly"), X, Y, custom_print="kernel=poly")

        # Support Vector Machine.
        ModelBenchmark.run(SVC(kernel="sigmoid"), X, Y, custom_print="kernel=sigmoid")

        # Linear Support Vector Machine.
        ModelBenchmark.run(LinearSVC(), X, Y, custom_print="Default")

        # Linear Support Vector Machine.
        ModelBenchmark.run(LinearSVC(multi_class="crammer_singer"), X, Y, custom_print="multi_class=crammer_singer")

        # 3-Nearest Neighbor.
        ModelBenchmark.run(KNeighborsClassifier(n_neighbors=3), X, Y, custom_print="n_neighbors=3")

        # 5-Nearest Neighbor.
        ModelBenchmark.run(KNeighborsClassifier(n_neighbors=5), X, Y, custom_print="n_neighbors=5")

        # 7-Nearest Neighbor.
        ModelBenchmark.run(KNeighborsClassifier(n_neighbors=7), X, Y, custom_print="n_neighbors=7")

        # 9-Nearest Neighbor.
        ModelBenchmark.run(KNeighborsClassifier(n_neighbors=9), X, Y, custom_print="n_neighbors=9")

        # Naive Bayes classifier for multinomial models.
        ModelBenchmark.run(MultinomialNB(), X, Y)

        # Naive Bayes classifier for multivariate Bernoulli models.
        ModelBenchmark.run(BernoulliNB(), X, Y)

        # Gaussian Naive Bayes
        ModelBenchmark.run(GaussianNB(), X, Y)

        # Gradient Boosting
        ModelBenchmark.run(GradientBoostingClassifier(), X, Y, custom_print="Default")

        # Gradient Boosting
        ModelBenchmark.run(GradientBoostingClassifier(max_depth=5), X, Y, custom_print="max_depth=5")

        # Gradient Boosting
        ModelBenchmark.run(GradientBoostingClassifier(max_depth=7), X, Y, custom_print="max_depth=7")

        # Random Forest
        ModelBenchmark.run(RandomForestClassifier(), X, Y, custom_print="Default")

        # Random Forest
        ModelBenchmark.run(RandomForestClassifier(n_estimators=50), X, Y, custom_print="n_estimators=50")

        # Random Forest
        ModelBenchmark.run(RandomForestClassifier(n_estimators=100), X, Y, custom_print="n_estimators=100")

        # MLP
        ModelBenchmark.run(MLPClassifier(), X, Y, custom_print="Default")

        # MLP
        ModelBenchmark.run(MLPClassifier(activation="identity"), X, Y, custom_print="activation=identity")

        # MLP
        ModelBenchmark.run(MLPClassifier(activation="logistic"), X, Y, custom_print="activation=logistic")

        # MLP
        ModelBenchmark.run(MLPClassifier(activation="tanh"), X, Y, custom_print="activation=tanh")

        # Stochastic Gradient Descent
        ModelBenchmark.run(SGDClassifier(), X, Y, custom_print="Default")

        # Stochastic Gradient Descent
        ModelBenchmark.run(SGDClassifier(shuffle=True), X, Y, custom_print="shuffle=True")

        # Decision Tree Classifer
        ModelBenchmark.run(DecisionTreeClassifier(), X, Y)

        ModelBenchmark.run(
            VotingClassifier(
                estimators=[
                    ('svm', SVC()),
                    ('knn', KNeighborsClassifier(n_neighbors=9)),
                    ('gb', GradientBoostingClassifier(max_depth=5)),
                    ('mlp', MLPClassifier(activation="tanh"))
                ],
                voting='hard'
            ),
            X, Y, custom_print="voting=hard"
        )
