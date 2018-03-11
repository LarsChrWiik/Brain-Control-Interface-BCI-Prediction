import unittest
from GUI.API import Filter
import numpy as np
from GUI import Importer

"""
This isnt running yet but looks like a more manedgble way to runs tests.
iv'e read they need to be in a folder named test and have test in the
class name. Il look more into it tomorrow.
"""

class TestFilter(unittest.TestCase):
    def filter(data_raw: dict, sigma: int=1, verbose=False) -> dict:
        isinstance(data_raw, dict)
        isinstance(sigma, int)
        isinstance(verbose, bool)

