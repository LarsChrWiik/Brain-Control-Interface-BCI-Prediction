import unittest

from API.Preprocessing import Filter

"""
This isnt running yet but looks like a more manedgble way to runs tests.
iv'e read they need to be in a folder named test and have test in the
class name. Il look more into it tomorrow.
"""

class TestFilter(unittest.TestCase):

    def setUp(self):
        Filter.Filter.filter()


