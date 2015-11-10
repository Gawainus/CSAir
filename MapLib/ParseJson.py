__author__ = 'yumentsao'

import json
import os
import Metro
import Arc


def parse(inFilePath):

    """
    :param inFilePath:
    :return:
    """

    fPath = os.path.abspath(os.path.join(os.pardir, inFilePath))
    inf = open(fPath, 'r')
    inputStr = inf.read()

    data = json.loads(inputStr)

    networkDict = dict()
    metros = dict()
    arcs = dict()

    networkDict["data sources"] = list()
    for source in data["data sources"]:
        networkDict["data sources"].append(source)


    for metro in data["metros"]:
        currMetro = Metro.Metro(metro)
        metros[currMetro.code] = currMetro

    for route in data["routes"]:
        currArc = Arc.Arc(route)
        arcKey = (currArc.origin, currArc.desti)
        arcs[arcKey] = currArc

    networkDict["metros"] = metros
    networkDict["arcs"] = arcs
    return networkDict


if __name__ == '__main__':

    cwd = os.getcwd()
    networkDict = parse("Data/Input.JSON")
    for metro in networkDict["metros"].items():
        print metro

    for arc in networkDict["arcs"].items():
        print arc[1].origin
