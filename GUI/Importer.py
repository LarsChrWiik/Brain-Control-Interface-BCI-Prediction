
import scipy.io

# Importing files.
class Importer:

    # Import information from a mat file.
    # Usable for both training and test files.
    @staticmethod
    def mat(filename):
        data = scipy.io.loadmat(filename)
        data = dict(data)
        try:
            del data["__globals__"]
            del data["__header__"]
            del data["__version__"]
            del data["StimulusCode"]

            # Only for train.
            del data["TargetChar"]
        except:
            pass

        # *** Signal = 3D array ***
        # 1: 85 examples.
        # 2: 7794 = time step.
        # 3: 64 sensor readings.

        # *** Flashing = 2D array ***
        # Definition: 0 or 1 depending on flashig.
        # 85 examples.
        # 7794 = time step.

        # *** TargetChar = 1D array with 1 row and 1 column***
        # Definition: letters in the alphabet.

        # *** StimulusType = 2D array
        # Definition: 0 or 1 meaning if the object flashed
        # 85 examples.
        # 7794 time step.

        # *** StimulusCode ***
        # Definition: which column or row flashed.

        return data