from contracts import *
from my_python.archive.a3.House import House

class HomesElem:
    @contract
    def __init__(self, h, uip):
        """
            Initialize HomesElem object (element in Homes) for each home in a homes list.

            :param h: House object representing the house on the home's property.
            :type h: valid_house

            :param uip: Boolean representing whether the home has been used in a plan already.
            :type uip: valid_used_in_plan
        """
        self.house = House(h)
        self.used_in_plan = uip

        assert not(not self.house.is_built() and self.get_used_in_plan()), "An unbuilt House cannot be used in a plan"

    @contract
    def get_house(self) -> House:
        """
            Returns House object in the Home.

            :return: House object
        """
        return self.house

    @contract
    def get_used_in_plan(self):
        """
            Returns whether or not the house was used in a plan.

            :type: None

            :return: Boolean representing whether or not the home was used in a plan.
            :rtype: bool
        """
        return self.used_in_plan

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, HomesElem):
            return (self.house == other.house
                    and self.used_in_plan == other.used_in_plan)
        return False
