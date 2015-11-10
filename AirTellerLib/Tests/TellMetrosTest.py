__author__ = 'yumentsao'


import unittest
from MapLib import ParseJson


class TestTellMetrosFunction(unittest.TestCase):
    networkDict = ParseJson.parse("../Data/Input.JSON")

    def setUp(self):
        print("Setting up")


    def tearDown(self):
        print("All Tests Run")

    # FIXIT: feed input to the test

# Run the unittests
if __name__ == '__main__':
    unittest.main()