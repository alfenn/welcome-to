from contracts import *
from my_python.a3_1.HomesElem import HomesElem

class Homes:
    @contract
    def __init__(self, homes_val):
        """
            Initialize Homes object from homes (list of homes) input.

            :param homes_val: Homes array
            :type homes_val: valid_homes
        """
        self.homes_and_fences = [True]  # leftmost fence exists
        self.homes_and_fences.append(HomesElem(homes_val[0], homes_val[1]))
        for i in range(len(homes_val)):
            if i >= 2:
                self.homes_and_fences.append(homes_val[i][0])
                self.homes_and_fences.append(HomesElem(homes_val[i][1], homes_val[i][2]))
                # DO NOT USE += BECAUSE IT EXPECTS THE THING AFTER IT TO BE AN ITERABLE
                #   https://stackoverflow.com/questions/2022031/python-append-vs-operator-on-lists-why-do-these-give-different-results
                # self.rest_homes += HomesElem(homes_val[i][0], homes_val[i][1], homes_val[i][2])
        self.homes_and_fences.append(True)

        ### Validate the ascending order of houses ###


        # for i in range
        # if house is bis, check house before and after
        # if bis house does not match a number of before or after, error
        # 2nd case: bis next to bis


        ### Validate that bis's are next to a house of the same number ###

        ### Validate that there are no duplicate houses ###
            ## add every house that is not a blank to the array
            ## outside the loop, check if array is sorted lowest to (or equal) biggest


        ### Validate that there are no fences separating "duplicate" houses ###


    @contract
    def get(self, i: int) -> HomesElem:
        """
            Get the homes

            :param i: Which home we are on
            :return: An array of 3 elements (or 2, if i==0) representing a 'Home'
        """
        assert 0 <= i < self.get_num_houses(), "requesting invalid index for HomesElem"
        return self.homes_and_fences[i*2 + 1]

    @contract
    def get_num_houses(self) -> int:
        """
            Get the number of houses on the street we are on

            :return: An int representing the number of houses on the street
            :rtype: int
        """
        return len(self.homes_and_fences)//2

    @contract
    def validate_bis(self) -> bool:
        """
            Validate that a bis is next to a house with an identical number in O(N).

            :return: True when all homes are validated
            :rtype: bool
        """
        all_homes = []
        bis_counter = 0
        ## add blank checks
        ## check bis_counter[1] and bis_counter[-1]
        # Fill all_homes array with EVERY home (built, blank, bis)
        for i in range(self.get_num_houses()):
            curr_home = self.get(i).get_house()
            all_homes.append(curr_home)

        for i in range(len(all_homes)):
            temp_bis_counter = 0
            # Define current_house, house before current_house, and house after current_house
            curr_home = self.get(i).get_house()
            if i > 0:
                curr_home_bef = self.get(i - 1).get_house()
            if i < self.get_num_houses() - 1:
                curr_home_aft = self.get(i + 1).get_house()
            # EDGE 1: If the current home is a bis and we are on the first home
            if curr_home.is_bis() and i == 0:
                # if the current home is the same number as the home after it, continue
                if curr_home.get_num() == curr_home_aft.get_num():
                    # if house after current is a bis, increment bis_counter; else, set bis_counter = 0
                    if curr_home_aft.is_bis():
                        temp_bis_counter += 1
                    else:
                        temp_bis_counter = 0
                    continue
                # else, error
                else:
                    raise AssertionError
            # MAIN: If the current home is not the first or last home and is a bis
            if curr_home.is_bis():
                # if the current home is the same number as the home before or after it, continue
                if curr_home.get_num() == curr_home_bef.get_num():
                    # if house after current is a bis, increment bis_counter; else, set bis_counter = 0
                    if curr_home_bef.is_bis():
                        temp_bis_counter += 1
                    else:
                        temp_bis_counter = 0
                    continue
                elif curr_home.get_num() == curr_home_aft.get_num():
                    # if house after current is a bis, increment bis_counter; else, set bis_counter = 0
                    if curr_home_aft.is_bis():
                        temp_bis_counter += 1
                    else:
                        temp_bis_counter = 0
                    continue
                # else, error
                else:
                    raise AssertionError

            # EDGE 2: If the current home is a bis and we are on the last home
            if curr_home.is_bis() and i == self.get_num_houses - 1:
                # if the current home is the same number as the home after it, continue
                if curr_home.get_num() == curr_home_bef.get_num():
                    # if we have not hit a house that is not a bis yet, we increment bis_counter
                        # EDGE: this is to catch the case where all houses are bis'd
                    if curr_home_bef.is_bis() and bis_counter > 0:
                        raise AssertionError
                    continue
                # else, error
                else:
                    raise AssertionError
            bis_counter += temp_bis_counter
        # EDGE 3: If there are no normal houses, aka there are only bis'd houses, we error
        if bis_counter > 0:
            raise AssertionError

        return True

    def validate_ascending_order(self) -> bool:
        """
            Validate ascending order of the built houses.
            :return: True if order is ascending, False if it's not ascending
        """
        # Get built houses
        built_houses = []
        for i in range(self.get_num_houses()):
            curr_house = self.get(i).get_house()
            if curr_house.is_bis():
                built_houses.append(curr_house)
        i = 1
        while i < len(built_houses):
            house1 = self.get(i).get_house()
            house2 = self.get(i-1).get_house()
            # If either house is a bis
            if house1.is_bis() or house2.is_bis():
                # Return False if the pair of Houses doesn't satisfy the <= condition
                if house1.get_num() <= house2.get_num(): raise AssertionError("the pair of homes (at least one is a bis) doesn't satisfy the <= condition")
            # If neither house is a bis
            else:
                if house1.get_num() < house2.get_num(): raise AssertionError("the pair of homes (neither is a bis) doesn't satisfy the < condition")
            i += 1
        return True

