__author__ = 'yumentsao'

import time

from MapLib import ParseJson
from MapLib import AirNetwork

from AirManageLib import ManageNetwork


def AirTeller():
    """
    The main loop of the CSAir Management Teller Machine

    :return: Print out query result to the screen
    """
    networkDict = ParseJson.parse("CSAir/Data/Input.JSON")
    network = AirNetwork.AirNetwork(networkDict)

    while True:
        print "Welcome to CSAir Management Gateway!"
        staffCode = raw_input("Please enter your staff code: ")
        print("\nHello " + staffCode + ".\n")
        print("You have the following options:")
        print("1. Manage.\n"
              "2. View Network as a customer.\n")

        while True:
            try:
                actionNumberStr = raw_input("What can I do for ya? (Enter the "
                                            "number of the action you would "
                                            "like to perform)")
                actionNumber = int(actionNumberStr)
            except:
                print("Your input is not a number.")
            else:
                break

        if actionNumber == 1:
            ManageNetwork.performAction(network)

        elif actionNumber == 2:
            print("Connecting you to the AirTeller Machine")

        else:
            print("Please choose between 1 and 2.")
            time.sleep(1)

        satisfaction = raw_input("Do you like the current management system? "
                                 "(Y/N)")
        if satisfaction.upper() == "N":
            print("You are fired.\n\n")
        elif satisfaction.upper() == "Y":
            print("Thanks for using CSAir Management Gateway.\n\n")
        else:
            print("You answer Y or N. Geez!\n\n")
        time.sleep(3)

if __name__ == '__main__':
    AirTeller()
