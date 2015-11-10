__author__ = 'yumen'

import unittest

from MapLib import ParseJson
from MapLib import AirNetwork
from DijkstraLib import DijkstraGraph


class testDijkstraAlgorithm(unittest.TestCase):

    networkDict = ParseJson.parse("../Data/SmallGraph.JSON")
    network = AirNetwork.AirNetwork(networkDict)

    sGgraph = DijkstraGraph.DijkstraGraph(network)

    networkDict = ParseJson.parse("../Data/Input.JSON")
    network = AirNetwork.AirNetwork(networkDict)

    lGgraph = DijkstraGraph.DijkstraGraph(network)

    def setUp(self):
        print("Setting up")

    def tearDown(self):
        print("All Tests Run")

    def testSmallGraph(self):
        dg = self.__class__.sGgraph

        dg.initNodes()
        dg.runDijkstra(dg.nodes["1"])

        dg.printPath(dg.nodes["1"], dg.nodes["5"])
        self.assertEqual(dg.nodes["5"].dist, 20)

        dg.printPath(dg.nodes["1"], dg.nodes["4"])
        self.assertEqual(dg.nodes["4"].dist, 20)

    def testLargeGraph(self):
        dg = self.__class__.lGgraph

        dg.initNodes()
        dg.runDijkstra(dg.nodes["LAX"])

        dg.printPath(dg.nodes["LAX"], dg.nodes["MIA"])
        dg.printPath(dg.nodes["LAX"], dg.nodes["CHI"])

        dg.runDijkstra(dg.nodes["LON"])
        dg.printPath(dg.nodes["LON"], dg.nodes["LAX"])

        dg.runDijkstra(dg.nodes["HKG"])
        dg.printPath(dg.nodes["HKG"], dg.nodes["LAX"])



# Run the unittests
if __name__ == '__main__':
    unittest.main()

