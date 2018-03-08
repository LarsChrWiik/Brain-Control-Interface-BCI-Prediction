from sklearn.metrics import cohen_kappa_score, recall_score, accuracy_score, precision_score, f1_score, precision_recall_fscore_support

"""
Statistical data collection for the prediction model.
"""
class PredictionModelStatistics:

    accuracy = None
    precision = None
    recall = None
    f1 = None
    support = None
    kappa = None

    def fill(self,testing_target, prediction_final ):
        self.recall = recall_score(testing_target, prediction_final)
        self.accuracy = accuracy_score(testing_target, prediction_final)
        self.precision = precision_score(testing_target, prediction_final)
        self.f1 = f1_score(testing_target, prediction_final)
        self.support = precision_recall_fscore_support(testing_target, prediction_final)
        self.kappa = cohen_kappa_score(testing_target, prediction_final)
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
