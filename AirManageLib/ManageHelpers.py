__author__ = 'yumen'


import time


def endTelling():
    wantAnother = raw_input("Would you like to perform another action? (Y/N)\n")

    if wantAnother.upper() == "N":
        return True
    else:
        time.sleep(1)
        return False
