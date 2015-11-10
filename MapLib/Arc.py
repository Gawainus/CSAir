__author__ = 'yumentsao'


class Arc:
    """
    The class of Arc including
    origin
    destination
    distance in between
    """
    def __init__(self, arcJson):
        self.origin = arcJson["ports"][0]
        self.desti = arcJson["ports"][1]
        self.dist = arcJson["distance"]
