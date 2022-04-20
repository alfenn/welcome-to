from my_python.a3_1.my_contracts_PlayerState import *

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
    def is_bis(self):
        """
            Tells you whether the property is a bis or not.

            :type: None

            :return: Valid_bis which represents whether the property is a 'bis'
            :rtype: valid_bis
        """
        return self.is_bis

    @contract
    def get_num(self):
        """
            Returns -1 if it's not built, else returns the num for the house.

            :type: None

            :return: A Boolean that represents whether the house is built.
            :rtype: bool
        """
        return self.num
