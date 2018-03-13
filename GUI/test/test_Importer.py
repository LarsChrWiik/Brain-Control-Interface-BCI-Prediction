import unittest
import Importer

class testImporter(unittest.TestCase):
    def setUp(self):
        self.assertIsInstance(Importer.Importer.mat("Subject_A_Train.mat"),
                              dict, "Searching for Subject_A_Train.mat in root dir, if" +
                                    "not there this test will fail.")

