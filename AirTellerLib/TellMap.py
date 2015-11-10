__author__ = 'yumentsao'

import webbrowser

mapURL = "http://www.gcmap.com/mapui?P="


def tellMap(netowrk):
    """

    :param netowrk:
    :return:
    """

    queryValues = ""
    for arc in netowrk.arcs:
        queryValues += arc[0] + "-" + arc[1] + ","

    queryURL = mapURL + queryValues
    webbrowser.open(queryURL)
    return
