import unittest
import API.Randomizer as r

class testRandomizer(unittest.TestCase):
    def test_shuffle_two_lists_test(lista, listb):
        unittest.assertIsInstance(lista, list)
        unittest.assertIsInstance(listb, list)
        a, b = r.Randomizer.shuffle_two_lists(lista, listb)
        unittest.assertIsInstance(a, list)
        unittest.assertIsInstance(b, list)


