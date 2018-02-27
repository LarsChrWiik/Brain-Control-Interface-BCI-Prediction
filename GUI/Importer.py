
import scipy.io

"""
Class used to import dataset file types. 
Every function must return a dictionary. 
    if TRAIN, then the dict should contain:
        - StimulusType
        - Signal
        - Flashing
    if TEST, then the dict should contain:
        - Flashing
        - Signal
"""
class Importer:

    """
    Import information from a mat file.
    This function is compatible for both training and test files.
    """
    @staticmethod
    def mat_train(filename):
        data = scipy.io.loadmat(filename)
        data = dict(data)

        # Remove indexes from train and test.
        try:
            del data["__globals__"]
            del data["__header__"]
            del data["__version__"]
            del data["StimulusCode"]
        except:
            pass

        # Remove indexes from train.
        try:
            del data["TargetChar"]
        except:
            pass

        return data
