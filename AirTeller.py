__author__ = 'yumentsao'

import time

from MapLib import ParseJson
from MapLib import AirNetwork

from AirTellerLib import TellMetros
from AirTellerLib import TellFacts
from AirTellerLib import TellMap


def AirTeller():
    """
    The main loop of the CSAir Automatic Teller Machine

    :return: Print out query result to the screen
    """
    networkDict = ParseJson.parse("CSAir/Data/Input.JSON")
    network = AirNetwork.AirNetwork(networkDict)

    while True:
        print "Welcome to CSAir!"
        userName = raw_input("Please enter your name: ")
        print("\nHello " + userName + ".\n")
        print("You have the following options:")
        print("1. A list of all cities.\n"
              "2. CSAir Service Facts.\n"
              "3. See our network in a browser.\n")

        while True:
            try:
                actionNumberStr = raw_input("What can I do for ya? (Enter the number of "
                          "the action you would like to perform)")
                actionNumber = int(actionNumberStr)
            except:
                print("Your input is not a number.")
            else:
                break

        if actionNumber == 1:
            TellMetros.tellMetros(network)

        elif actionNumber == 2:
            TellFacts.tellFacts(network)

        elif actionNumber == 3:
            TellMap.tellMap(network)
        else:
            print("Please choose from 1, 2 and 3.")
            time.sleep(1)

        satisfaction = raw_input("Are you happy with our service? (Y/N)")
        if satisfaction.upper() == "N":
            print("Customers' feedback is BS anyway.\n\n")
        elif satisfaction.upper() == "Y":
            print("Thanks for choosing CSAir.\n\n")
        else:
            print("You answer Y or N. Geez!\n\n")
        time.sleep(3)

if __name__ == '__main__':
    AirTeller()
