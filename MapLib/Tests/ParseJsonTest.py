__author__ = 'yumentsao'

import unittest
from MapLib import ParseJson


class TestParseFunction(unittest.TestCase):
    networkDict = ParseJson.parse("../Data/Input.JSON")

    def setUp(self):
        print("Setting up")

    def tearDown(self):
        print("All Tests Run")

    def testKeyType(self):
        self.assertEqual(type(self.__class__.networkDict["arcs"]), dict)
        self.assertEqual(type(self.__class__.networkDict["metros"]), dict)
        self.assertEqual(type(self.__class__.networkDict["data sources"]), list)


# Run the unittests
if __name__ == '__main__':
    unittest.main()
