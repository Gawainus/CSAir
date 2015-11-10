__author__ = 'yumentsao'

import sys
import operator
from collections import defaultdict
import TellerHelpers


def longestSingleFlight(network):
    """

    :param network:
    :return:
    >>> networkDict = ParseJson.parse("Data/Input.JSON")
    >>> network = AirNetwork.AirNetwork(networkDict)
    >>> longestSingleFlight(network)
    The longest single flight: 12051
    >>>
    """
    longestArc = 0
    for arc in network.arcs.items():
        if longestArc < arc[1].dist:
            longestArc = arc[1].dist
    print("The longest single flight: " + str(longestArc) + "\n")


def shortestSingleFlight(network):
    """

    :param network:
    :return:
    >>> networkDict = ParseJson.parse("Data/Input.JSON")
    >>> network = AirNetwork.AirNetwork(networkDict)
    >>> shortestSingleFlight(network)
    The shortest single flight: 334
    <BLANKLINE>
    """
    shortestArc = sys.maxint
    for arc in network.arcs.items():
        if shortestArc > arc[1].dist:
            shortestArc = arc[1].dist
    print("The shortest single flight: " + str(shortestArc) + "\n")


def avgDist(network):
    count = 0
    total = 0
    for arc in network.arcs.items():
        total += arc[1].dist
        count += 1
    mean = total / count
    print("The average distance of flights: " + str(mean) + "\n")


def biggestCity(network):
    biggestPopulation = 0
    metroName = ""
    for metro in network.metros.items():
        if biggestPopulation < metro[1].population:
            biggestPopulation = metro[1].population
            metroName = metro[1].name
    print("The biggest city by population: " + metroName + " with "
          + str(biggestPopulation) + " people.\n")


def smallestCity(network):
    smallestPopulation = sys.maxint
    metroName = ""
    for metro in network.metros.items():
        if smallestPopulation > metro[1].population:
            smallestPopulation = metro[1].population
            metroName = metro[1].name
    print("The smallest city by population: " + metroName + " with " +
          str(smallestPopulation) + " people.\n")


def avgSize(network):
    total = 0
    count = 0
    for metro in network.metros.items():
        total += metro[1].population
        count += 1
    mean = total / count
    print("The avg population across all cities: " + str(mean) + "\n")


def listContinents(network):
    contis = defaultdict(list)
    for metro in network.metros.items():
        conti = metro[1].continent
        city = metro[1].name
        contis[conti].append(city)

    print("Exciting Continents we cover: ")
    for conti in contis.items():
        print (conti[0])

        for city in conti[1]:
            print(city + " "),
        print("\n")  # give it a new line


def listHubCities(network):
    origins = defaultdict(int)
    destis = defaultdict(int)

    for arc in network.arcs.items():
        origins[arc[0][0]] = 0
        destis[arc[0][1]] = 0

    for arc in network.arcs.items():
        origins[arc[0][0]] += 1
        destis[arc[0][1]] += 1

    sortedOrigins = sorted(origins.items(), key=operator.itemgetter(1),
                           reverse=True)
    sortedDestis = sorted(destis.items(), key=operator.itemgetter(1),
                          reverse=True)

    print("Exciting Hub Cities we cover: ")


    print("Top 10 Arrival Hubs:")
    for i in range(0, 10):
        cityCode = sortedOrigins[i][0]
        cityName = network.metros[cityCode].name
        numDeparture = sortedOrigins[i][1]
        print(cityName + ": " + str(numDeparture) +" flights departing here.")

    print("\nTop 10 Arrival Hubs:")
    for i in range(0, 10):
        cityCode = sortedDestis[i][0]
        cityName = network.metros[cityCode].name
        numArrival = sortedOrigins[i][1]
        print(cityName + ": " + str(numArrival) +" flights arriving here.")
    print("\n")


dispatch = {
    "1": longestSingleFlight,
    "2": shortestSingleFlight,
    "3": avgDist,
    "4": biggestCity,
    "5": smallestCity,
    "6": avgSize,
    "7": listContinents,
    "8": listHubCities
}


def tellFacts(network):
    while True:

        print("1. What is the longest single flight in the network?\n"
              "2. What is the shortest single flight in the network?\n"
              "3. What is the average distance of all the flights in the network?\n"
              "4. What is the biggest city (by population) served by CSAir?\n"
              "5. What is the smallest city (by population) served by CSAir?\n"
              "6. What is the average size (by population) of all cities served by CSAir?\n"
              "7. A list of continents served by CSAir and cities in them.\n"
              "8. A list of Hub Cities")

        factNumber = raw_input("What would you like to know about us?")
        try:
            dispatch[factNumber](network)
        except ValueError:
            print("\nPlease Enter a number between 1 and 8.\n")
            continue

        if TellerHelpers.endTelling():
            return

if __name__ == '__main__':
    from MapLib import ParseJson, AirNetwork
    import doctest
    doctest.testmod()

    networkDict = ParseJson.parse("Data/Input.JSON")
    network = AirNetwork.AirNetwork(networkDict)
    longestSingleFlight(network)
    shortestSingleFlight(network)
