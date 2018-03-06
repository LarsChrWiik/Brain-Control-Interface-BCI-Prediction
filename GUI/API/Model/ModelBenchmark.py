from sklearn.model_selection import cross_val_score
from sklearn.metrics import cohen_kappa_score, classification_report
from sklearn.model_selection import train_test_split

class ModelBenchmark:

    @staticmethod
    def run(classifier, X, Y, test_size=0.3, k_fold=10):
        # Model name.
        model_name = type(classifier).__name__

        # Divide into training and test set.
        training_input, testing_input, training_target, testing_target = train_test_split(
            X,
            Y,
            test_size=test_size
        )

        # Cross validation.
        cv = cross_val_score(classifier, X, Y, cv=k_fold)
        cv_avg = round((sum(cv) / len(cv)), 3)

        # Fit.
        classifier.fit(training_input, training_target)

        # Predict.
        prediction = classifier.predict(testing_input)

        # Generate report.
        report = classification_report(testing_target, prediction)

        # Calculate kappa.
        kappa = cohen_kappa_score(testing_target, prediction)

        count_0 = len([i for i in prediction if i == 0])
        count_1 = len([i for i in prediction if i == 1])

        # Print information.
        print("***** " + str(model_name) + " : " + str(cv_avg) + " *****")
        print("Cross-Validation = " + str(cv))
        print("Kappa = " + str(kappa))
        print("Number of 0 in prediction = " + str(count_0))
        print("Number of 1 in prediction = " + str(count_1))
        print(report)
        print("")
