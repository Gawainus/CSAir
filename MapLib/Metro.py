__author__ = 'yumentsao'

import json

class Metro:

    """
    To get latitude and longitude do:
    json.loads(coordinates)
    """

    def __init__(self, metroJson):

        """

        :param metroJson:
        :return:
        """
        # metroJson = json.loads(metroJsonStr)
        self.code = metroJson["code"]
        self.name = metroJson["name"]
        self.country = metroJson["country"]
        self.continent = metroJson["continent"]
        self.timezone = metroJson["timezone"]
        self.coordinates = metroJson["coordinates"]
        self.population = metroJson["population"]
        self.region = metroJson["region"]

