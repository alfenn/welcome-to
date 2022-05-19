from my_python.archive.a3.my_contracts_PlayerState import *

class House:
    @contract
    def __init__(self, in_house):
        """
            Initialize 'House' object from house input.

            :param in_house: Could be any of the three values that a house type could take
            :type in_house: valid_house
        """
        self.is_bis = False
        self.num = -1

        if isinstance(in_house, list):
            self.is_bis = True
            self.num = in_house[0]
        elif isinstance(in_house, int):
            self.is_bis = False
            self.num = in_house
        # Could just be an `else`
        elif isinstance(in_house, str):
            self.is_bis = False
            self.num = -1

        if self.is_built():
            assert 0 <= self.get_num() <= 17, "a valid_house number must be between 0 and 17"

    @contract
    def is_built(self):
        """
            Tells you whether the house is built or not.
            If it's not built, it is also not a bis.

            :type: None

            :return: A Boolean that represents whether the 'House' is built or not.
            :rtype: bool
        """
        return self.num != -1

    @contract
    def get_is_bis(self):
        """
            Tells you whether the property is a bis or not.

            :type: None

            :return: Valid_bis which represents whether the property is a 'bis'
            :rtype: bool
        """
        return self.is_bis

    @contract
    def get_num(self):
        """
            Returns -1 if it's not built, else returns the num for the house.

            :type: None

            :return: A number representing the house number
            :rtype: int
        """
        return self.num

    def get_val(self):
        """
            Gets the value for a house (either it's number, or "blank", or [num, "bis"])
            :return: int or "blank" or [num, "bis"]
        """
        if self.num == -1: return "blank"
        if self.is_bis: return [self.num, "bis"]
        return self.num

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, House):
            return (self.is_bis == other.is_bis
                    and self.num == other.num)
        return False
