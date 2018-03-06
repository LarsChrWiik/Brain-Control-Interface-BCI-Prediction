
from API.Model.ModelBenchmark import ModelBenchmark
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB

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

        # Naive Bayes classifier for multinomial models.
        ModelBenchmark.run(MultinomialNB(), X, Y)

        # Naive Bayes classifier for multivariate Bernoulli models.
        ModelBenchmark.run(BernoulliNB(), X, Y)




        # TODO: Test more...




# TODO: REMOVE.
"""
# Validate performance.
score = cross_val_score(clf, X, Y, cv=3)
print("Cross_val = " + str(score))

# Fit the model.
clf.fit(X_train, y_train)

# Predict test set.
predictions = clf.predict(X_test)

print("predictions = " + str(predictions))

# Precision.
print("Precision = " + str(average_precision_score(y_test, predictions)))

# Recall.
print("Recall = " + str(recall_score(y_test, predictions)))
"""
