
import scipy.io

# Importing files.
class Importer:

    # Import information from a mat file.
    # Usable for both training and test files.
    @staticmethod
    def mat(filename):
        mat = scipy.io.loadmat(filename)
        mat = dict(mat)
        try:
            del mat["__globals__"]
            del mat["__header__"]
            del mat["__version__"]
            del mat["StimulusCode"]

            # Only for train.
            del mat["TargetChar"]
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

        return mat