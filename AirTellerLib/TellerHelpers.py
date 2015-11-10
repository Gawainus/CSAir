__author__ = 'yumentsao'


import time


def endTelling():
    wantAnother = raw_input("Would you like to look up another fact? (Y/N)\n")

    if wantAnother.upper() == "N":
        return True
    else:
        time.sleep(1)
        return False
