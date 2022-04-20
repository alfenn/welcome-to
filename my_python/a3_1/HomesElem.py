import contracts
from contracts import *
from House import *

class HomesElem:
    @contract
    def __init__(self, fon, h, uip):
        """
            Initialize HomesElem object (element in Homes) for each home in a homes list.

            :param fon: Boolean representing whether there is a fence or not on the left of the home.
            :type fon: valid_fence_or_not

            :param h: House object representing the house on the home's property.
            :type h: valid_house

            :param uip: Boolean representing whether the home has been used in a plan already.
            :type uip: valid_used_in_plan
        """
        self.fence_or_not = fon
        self.house = House(h)
        self.used_in_plan = uip

    @contract
    def get_fence_or_not(self):
        """
            Returns whether there is a fence or not on the left side of the home.

            :type: None

            :return: Boolean representing whether there's a fence or not on the left side of the home.
            :rtype: valid_fence_or_not
        """
        return self.fence_or_not

    @contract
    def get_house(self):
        """
            Returns House object in the Home.

            :type: None

            :return: House object
            :rtype: valid_house
        """
        return self.house

    @contract
    def get_used_in_plan(self):
        """
            Returns whether or not the house was used in a plan.

            :type: None

            :return: Boolean representing whether or not the home was used in a plan.
            :rtype: valid_used_in_plan
        """
        return self.used_in_plan
