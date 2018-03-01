
import scipy.io
import numpy as np

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
    def mat(filename):
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

        # Transpose Signal.
        signals = np.array(data["Signal"])
        transposed_signals = []
        for i in range(len(signals)):
            new = np.transpose(signals[i])
            transposed_signals.append(new)
        data["Signal"] = np.array(transposed_signals)

        return data
