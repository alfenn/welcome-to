from contracts import *
from HomesElem import *

class Homes:
    @contract
    def __init__(self, homes_val):
        """
            Initialize Homes object from homes (list of homes) input.

            :param homes_val: Homes array
            :type homes_val: valid_homes
        """
        self.first_home = HomesElem(True, homes_val[0], homes_val[1])
        self.rest_homes = []
        for i in range(len(homes_val)):
            if i >= 2:
                self.rest_homes += HomesElem(homes_val[i][0], homes_val[i][1], homes_val[i][2])

    @contract
    def get(self, i):
        """
            Get the homes

            :param i: Which home we are on
            :type: None

            :return: An array of 3 elements representing a 'Home'
            :rtype: valid_homes_val_list

        """
        if i == 0:
            return self.first_home
        return self.rest_homes[i-1]