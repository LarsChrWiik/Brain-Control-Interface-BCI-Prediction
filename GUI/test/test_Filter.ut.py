import unittest
from GUI.API import Filter
import numpy as np
from GUI import Importer

"""
This isnt running yet but looks like a more manedgble way to runs tests.
iv'e read they need to be ina  fodler named test and have test in the
class name. Il look more into it tomorrow.
"""

class TestFilter(unittest.TestCase):
    def setup(self):
        filename_trian_A = "Subject_A_Train.mat"
        self.file = Importer.mat(filename_trian_A)
        self.func = Filter.filter(self.file)

    def test_1(self):
        self.assertIsInstance(self.func, np.ndarray)
        self.assertIsInstance(self.file, np.ndarray)

    def test_2(self):
        self.assertTrue(self.file)

if __name__ == '__main__':
    unittest.main()
