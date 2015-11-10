__author__ = 'yumentsao'

import sys
import operator
import pprint
import json

from collections import defaultdict

from MapLib import Metro
from MapLib import Arc

import ManageHelpers


def removeCity(network):
    code = raw_input("Please enter code of the city: ")
    try:
        del network.metros[code]
    except:
        print("This code is not in the current network\n")

def removeRoute(network):
    origin = raw_input("Please enter the origin: ")
    desti = raw_input("Please enter the desti: ")
    key = (origin, desti)
    try:
        del network.arcs[key]
    except:
        print("This route is not in the current network\n")

def addMetro(network, metroEntity):
    metro = Metro.Metro(metroEntity)
    network.metros[metro.code] = metro

def addRoute(network, routeEntity):
    arc = Arc.Arc(routeEntity)
    key = (arc.origin, arc.desti)
    network.arcs[key] = arc

def editMetroPop(network, code, novaValue):
    code = raw_input("Please enter code of the city: ")
    try:
        del network.metros[code]
    except:
        print("This code is not in the current network\n")
    network.metros[code].population = novaValue

def saveProgress(network):
    outDict = defaultdict()
    outDict["data sources"] = network.sources

    metroArr = []
    for metro in network.metros.items():
        metroEntity = defaultdict()
        metroEntity["code"] = metro[1].code
        metroEntity["name"] = metro[1].name
        metroEntity["country"] = metro[1].country
        metroEntity["continent"] = metro[1].continent
        metroEntity["timezone"] = metro[1].timezone
        metroEntity["coordinates"] = metro[1].coordinates
        metroEntity["population"] = metro[1].population
        metroEntity["region"] = metro[1].region
        metroArr.append(metroEntity)
    outDict["metros"] = metroArr

    routeArr = []
    for route in network.arcs.items():
        routeEntity = defaultdict()
        routeEntity["ports"] = []
        routeEntity["ports"].append(route[1].origin)
        routeEntity["ports"].append(route[1].desti)
        routeEntity["distance"] = route[1].dist
        routeArr.append(routeEntity)
    outDict["routes"] = routeArr

    fileStr = json.dumps(outDict, ensure_ascii=False)
    # pp = pprint.PrettyPrinter(indent=4)
    # ppFileStr = pp.pformat(fileStr)
    outFile = open("temp.JSON", 'w')
    outFile.write(fileStr)
    outFile.close()

dispatch = {
    "1": removeCity,
    "2": removeRoute,
    "3": addMetro,
    "4": addRoute,
    "5": editMetroPop,
    "6": saveProgress
}


def performAction(network):
    while True:

        print("1. Remove a city\n"
              "2. Remove a route\n"
              "3. Add a city\n"
              "4. Add a route\n"
              "5. Edit a city\n"
              "6. Save progress\n")

        factNumber = raw_input("What would you like to perform?")
        try:
            dispatch[factNumber](network)
        except ValueError:
            print("\nPlease Enter a number between 1 and 6.\n")
            continue

        if ManageHelpers.endTelling():
            return

if __name__ == '__main__':
    from MapLib import ParseJson, AirNetwork


    networkDict = ParseJson.parse("Data/Input.JSON")
    network = AirNetwork.AirNetwork(networkDict)
    saveProgress(network)

