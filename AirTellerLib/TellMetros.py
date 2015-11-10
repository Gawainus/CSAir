__author__ = 'yumentsao'


import TellerHelpers


def tellMetros(network):

    while True:

        for metro in network.metros.items():
            print(metro[1].code + " " + metro[1].name)
        code = raw_input("Would you like the details of a city? Enter its code to display.")
        code = code.upper()
        try:
            metro = network.metros[code]
        except:
            print("You must enter a valid code of the city.")
            continue

        print(metro.name + " " + metro.country + " " + metro.continent)
        print("GMT: " + str(metro.timezone))

        print("Coordinates:"),
        for coordi in metro.coordinates.items():
            print(coordi[0] + ": " + str(coordi[1])),

        print("Population: " + str(metro.population))
        print("Region: " + str(metro.region))

        if TellerHelpers.endTelling():
            return

if __name__ == '__main__':
    pass