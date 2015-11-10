__author__ = 'gawain'

import ParseJson


class AirNetwork:
    """
    This class defines the whole network of the airlines
    a dictionary of metros
    a dictionary of arcs

    """

    def __init__(self, networkDict):
        self.sources = networkDict["data sources"]
        self.metros = networkDict["metros"]
        self.arcs = networkDict["arcs"]

    def printMetros(self):
        for metro in network.metros.items():
            metroValue = metro[1]
            print (metroValue.code + " " + metroValue.name + " " + metroValue.country
                   + " " + str(metroValue.coordinates) + " " + str(metroValue.timezone) + " " + metroValue.continent + " "
                   + str(metroValue.population)+ " " + str(metroValue.region))

    def printArcs(self):
        for arc in network.arcs.items():
            arcValue = arc[1]
            print (arcValue.origin + " " + arcValue.desti + " " + str(arcValue.dist))


if __name__ == '__main__':
    networkDict = ParseJson.parse("Data/Input.JSON")
    network = AirNetwork(networkDict)

    network.printMetros()
    network.printArcs()
