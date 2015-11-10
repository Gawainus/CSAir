__author__ = 'yumen'

import collections
import Queue

import DijkstraNode

class DijkstraGraph:

    def __init__(self, network):
        self.nodes = collections.defaultdict()
        self.incompleteNodes = Queue.Queue()

        for metro in network.metros:
            self.nodes[metro] = DijkstraNode.DijkstraNode(metro, network)

    def initNodes(self):
        for node in self.nodes.items():
            node[1].initNode()

    def runDijkstra(self, src):
        self.initNodes()

        src.dist = 0
        currNode = src
        self.incompleteNodes.put(src)

        while self.incompleteNodes.qsize() > 0:
            if currNode is None:
                currNode = self.incompleteNodes.get()
            self.processNode(currNode)

            for outArc in currNode.outArcs:
                targetNode = self.nodes[outArc.desti]
                if not targetNode.out:
                    self.incompleteNodes.put(targetNode)
            currNode = currNode.findCheapestNeighbor(self)

    def processNode(self, currNode):
        if currNode.out:
            return

        print("Processing Node: " + currNode.code)
        for outArc in currNode.outArcs:
            targetNode = self.nodes[outArc.desti]
            tempDist = currNode.dist + outArc.dist

            if tempDist < targetNode.dist:
                print("To " + targetNode.code + ": " + str(tempDist))
                targetNode.dist = tempDist
                targetNode.prev = currNode

        currNode.out = True

    def printPath(self, src, sink):
        path = []
        currNode = sink
        prevNode = sink.prev

        path.append(sink.code)
        while prevNode != src:
            path.append(prevNode.code)
            currNode = currNode.prev
            prevNode = currNode.prev
        path.append(src.code)
        while len(path) > 0:
            print(path.pop() + " "),
        print


if __name__ == '__main__':
    from MapLib import ParseJson
    from MapLib import AirNetwork

    networkDict = ParseJson.parse("Data/Input.JSON")
    network = AirNetwork.AirNetwork(networkDict)

    dGgraph = DijkstraGraph(network)

    for dNode in dGgraph.nodes.items():
        print dNode[1].code

        for outArc in dNode[1].outArcs:
            print(outArc.origin)
            print(outArc.desti)
            print(outArc.dist)
