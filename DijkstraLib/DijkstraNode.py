__author__ = 'yumentsao'

import sys


class DijkstraNode:

    def __init__(self, code, network):
        self.code = code
        self.dist = sys.maxint
        self.prev = self
        self.out = False
        self.outArcs = []
        self.inArcs = []

        for arc in network.arcs.items():
            if self.code == arc[0][0]:
                self.outArcs.append(arc[1])
            if self.code == arc[0][1]:
                self.inArcs.append(arc[1])

    def initNode(self):
        self.dist = sys.maxint
        self.prev = self            # The best previous node so far
        self.out = False            # Whether this node is checked

    def findCheapestNeighbor(self, network):
        distToSrc = sys.maxint
        cheapestNeighbor = None

        for outArc in self.outArcs:
            cheapNeighbor = network.nodes[outArc.desti]
            if not cheapNeighbor.out and cheapNeighbor.dist < distToSrc:
                cheapestNeighbor = cheapNeighbor
                distToSrc = cheapNeighbor.dist
        return cheapestNeighbor


if __name__ == '__main__':
    from MapLib import ParseJson
    from MapLib import AirNetwork

    networkDict = ParseJson.parse("Data/cmi_hub.JSON")
    network = AirNetwork.AirNetwork(networkDict)

    node_1 = DijkstraNode(network.metros["CMI"].code, network)
    print(node_1.code)
    print(node_1.dist)

    print("Outbound flights")
    for outArc in node_1.outArcs:
        print outArc

    print("Inbound flights")
    for inArc in node_1.inArcs:
        print inArc
