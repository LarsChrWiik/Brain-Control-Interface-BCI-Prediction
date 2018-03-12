from sklearn.metrics import cohen_kappa_score, recall_score, accuracy_score, precision_score, f1_score, precision_recall_fscore_support

"""
Statistical data collection for the prediction model.
"""
class PredictionModelStatistics:

    def __init__(self):
        self.recall = None
        self.accuracy = None
        self.precision = None
        self.f1 = None
        self.support = None
        self.kappa = None

    def update(self, testing_target, prediction):
        if self.recall is None:
            self.recall = recall_score(testing_target, prediction)
        else:
            self.recall += recall_score(testing_target, prediction)
        if self.accuracy is None:
            self.accuracy = accuracy_score(testing_target, prediction)
        else:
            self.accuracy += accuracy_score(testing_target, prediction)
        if self.precision is None:
            self.precision = precision_score(testing_target, prediction)
        else:
            self.precision += precision_score(testing_target, prediction)
        if self.f1 is None:
            self.f1 = f1_score(testing_target, prediction)
        else:
            self.f1 += f1_score(testing_target, prediction)
        if self.support is None:
            self.support = precision_recall_fscore_support(testing_target, prediction)
        else:
            self.support += precision_recall_fscore_support(testing_target, prediction)
        if self.kappa is None:
            self.kappa = cohen_kappa_score(testing_target, prediction)
        else:
            self.kappa += cohen_kappa_score(testing_target, prediction)

    def finish(self, folds):
        self.recall /= folds
        self.accuracy /= folds
        self.precision /= folds
        self.f1 /= folds
        self.kappa /= folds

    """
    Clear the statistical history. 
    """
    def clear_statistics(self):
        self.accuracy = None
        self.precision = None
        self.recall = None
        self.f1 = None
        self.support = None
        self.kappa = None
