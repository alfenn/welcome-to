import json

from contracts import *
from my_python.archive.a3.HomesElem import HomesElem

class Homes:
    @contract
    def __init__(self, homes_val):
        """
            Initialize Homes object from homes (list of homes) input.

            :param homes_val: Homes array
            :type homes_val: valid_homes
        """
        self.homes_and_fences = [True]  # leftmost fence exists
        assert ((not isinstance(homes_val[0], bool)
                 and isinstance(homes_val[0], int)
                 and 0 <= homes_val[0] <= 17)
               or homes_val[0] == "blank"
               or (isinstance(homes_val[0], list)
                   and len(homes_val[0]) == 2
                   and (not isinstance(homes_val[0][0], bool)
                        and isinstance(homes_val[0][0], int)
                        and 0 <= homes_val[0][0] <= 17)
                   and homes_val[0][1] == "bis")) \
               , "first house's num is not valid"
        self.homes_and_fences.append(HomesElem(homes_val[0], homes_val[1]))
        for i in range(len(homes_val)):
            if i >= 2:
                assert len(homes_val[i]) == 3, "the length of each non-first home must be 3"
                assert isinstance(homes_val[i][0], bool), "fences must be bools"
                self.homes_and_fences.append(homes_val[i][0])
                self.homes_and_fences.append(HomesElem(homes_val[i][1], homes_val[i][2]))
                # DO NOT USE += BECAUSE IT EXPECTS THE THING AFTER IT TO BE AN ITERABLE
                #   https://stackoverflow.com/questions/2022031/python-append-vs-operator-on-lists-why-do-these-give-different-results
                # self.rest_homes += HomesElem(homes_val[i][0], homes_val[i][1], homes_val[i][2])
        self.homes_and_fences.append(True)

        ### Run methods for validation ###
        # trust it works because of testing for individual methods
        #   comment this for method testing
        self.validate_bis()
        self.validate_ascending_order()
        self.validate_no_dups()
        self.validate_no_fences_between_bis()

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
            Get the number of homes on the street we are on

            :return: An int representing the number of homes on the street
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
        curr_not_bis_house = None

        for i in range(self.get_num_houses()):
            curr_home = self.get(i).get_house()
            all_homes.append(curr_home)

        for i in range(len(all_homes)):
            # Define current_house, house before current_house, and house after current_house
            curr_home = self.get(i).get_house()
            if i > 0:
                curr_home_bef = self.get(i - 1).get_house()
            if i < self.get_num_houses() - 1:
                curr_home_aft = self.get(i + 1).get_house()

            # if the current_house is NOT a bis and is not "blank", save the current_house
            if not curr_home.get_is_bis() and curr_home.is_built():
                curr_not_bis_house = curr_home.get_num()
                if (0 < i <= self.get_num_houses() - 1) and (curr_not_bis_house == curr_home_bef.get_num() or curr_not_bis_house == curr_home_aft.get_num()) and bis_counter > 0:
                    bis_counter = 0
                continue

            # EDGE 1: If the current home is a bis and we are on the first home
            if curr_home.get_is_bis() and i == 0:
                # if the current home is the same number as the home after it, continue
                if curr_home.get_num() == curr_home_aft.get_num():
                    # if house after current is a bis, increment bis_counter; else, set bis_counter = 0
                    if curr_home_aft.get_is_bis():
                        # if the current_house's num equals the last saved not bis'd house,
                        #   keep counter at 0; else, add 1 to counter
                            bis_counter += 1
                    continue
                # else, error
                else:
                    raise AssertionError("current bis'd home does not match the house before or after")

            # MAIN: If the current home is not the first or last home and is a bis
            if curr_home.get_is_bis():
                # if the current home is the same number as the home before or after it, continue
                if curr_home.get_num() == curr_home_bef.get_num():
                    # if house after current is a bis, increment bis_counter; else, set bis_counter = 0
                    if curr_home_bef.get_is_bis():
                        # if the current_house's num equals the last saved not bis'd house,
                        #   keep counter at 0; else, add 1 to counter
                        if curr_home.get_num() == curr_not_bis_house:
                            bis_counter = 0
                        else:
                            bis_counter += 1
                        continue
                    continue
                elif curr_home.get_num() == curr_home_aft.get_num():
                    # if house after current is a bis, increment bis_counter; else, set bis_counter = 0
                    if curr_home_aft.get_is_bis():
                        # if the current_house's num equals the last saved not bis'd house,
                        #   keep counter at 0; else, add 1 to counter
                        if curr_home.get_num() == curr_not_bis_house:
                            bis_counter = 0
                        else:
                            bis_counter += 1
                        continue
                    continue
                # else, error
                else:
                    raise AssertionError("current bis'd home does not match the house before or after")

            # EDGE 2: If the current home is a bis and we are on the last home
            if curr_home.get_is_bis() and i == self.get_num_houses - 1:
                # if the current home is the same number as the home after it, continue
                if curr_home.get_num() == curr_home_bef.get_num():
                    # if the current_house's num equals the last saved not bis'd house,
                    #   keep counter at 0; else, add 1 to counter
                    if curr_home_bef.get_is_bis():
                        if curr_home.get_num() == curr_not_bis_house:
                            bis_counter = 0
                        else:
                            bis_counter += 1
                    continue
                # else, error
                else:
                    raise AssertionError("current bis'd home does not match the house before or after")
        # EDGE 3: If there are no normal homes, aka there are only bis'd homes, we error
        if bis_counter > 0:
            raise AssertionError("all homes cannot be bis")

        return True

    @contract
    def validate_ascending_order(self) -> bool:
        """
            Validate ascending order of the built homes.
            :return: True if order is ascending, Error if it's not ascending
        """
        # Get built homes
        built_houses = []
        for i in range(self.get_num_houses()):
            curr_house = self.get(i).get_house()
            if curr_house.is_built():
                built_houses.append(curr_house)
        i = 1
        while i < len(built_houses):
            house1 = built_houses[i]
            house2 = built_houses[i-1]
            # house1 = self.get(i).get_house()
            # house2 = self.get(i-1).get_house()
            if house1.get_num() < house2.get_num(): raise AssertionError("the pair of homes (neither is a bis) doesn't satisfy the < condition")
            i += 1
        return True

    @contract
    def validate_no_dups(self) -> bool:
        """
            Validate that there are no duplicate regular homes.
            :return: True if there are no duplicate homes, AssertionError otherwise.
        """
        # Get built non-bis homes
        built_non_bis_houses = []
        for i in range(self.get_num_houses()):
            curr_house = self.get(i).get_house()
            if curr_house.is_built() and not curr_house.get_is_bis():
                # Iterate through the built_non_bis_houses and check if curr_house
                #   is a duplicate of any homes we already added.
                for j in range(len(built_non_bis_houses)):
                    if curr_house == built_non_bis_houses[j]: raise AssertionError("duplicate non-bis homes found")
                # If no duplicates were found, add curr_house to built_non_bis_houses
                built_non_bis_houses.append(curr_house)
        return True

    ### Validate that there are no fences separating "duplicate" homes ###
    @contract
    def validate_no_fences_between_bis(self) -> bool:
        """
            Validate that there are no fences in between bis'd homes
            :return: True if there are no fences between bis'd homes, AssertionError otherwise.
        """
        i = 3   # Because of the first house
        while i < len(self.homes_and_fences):
            house1 = self.homes_and_fences[i].get_house()
            house2 = self.homes_and_fences[i - 2].get_house()
            # TODO: figure out how to make "has_fence_left/right" methods on the House class.
            if (house1.get_num() == house2.get_num()) and (house1.is_built() and house2.is_built()):
                assert self.homes_and_fences[i - 1] is False, "cannot be fence between two bis's"
            i += 2
        return True

    @contract
    def get_num_non_bis_houses(self) -> int:
        """
            Get the number of non-bis homes
            :return: int representing the number of non-bis homes.
        """
        num_built_non_bis_houses = 0
        for i in range(self.get_num_houses()):
            curr_house = self.get(i).get_house()
            if curr_house.is_built() and not curr_house.get_is_bis():
                num_built_non_bis_houses += 1
        return num_built_non_bis_houses

    @contract
    def get_num_built_fences(self) -> int:
        """
            Get the number of built fences
            :return: int representing the number of built fences.
        """
        i = 0
        count_built_fences = 0
        while i < len(self.homes_and_fences):
            if self.homes_and_fences[i] is True: count_built_fences += 1
            i += 2
        return count_built_fences

    def has_left_fence(self, h_i: int) -> bool:
        """
            Tells us whether the given house has a left fence.

            :param h_i: index for the house in question
            :return: if the left fence exists (aka the left fence value)
        """
        return self.homes_and_fences[h_i * 2]

    def has_right_fence(self, h_i: int) -> bool:
        """
            Tells us whether the given house has a right fence.

            :param h_i: index for the house in question
            :return: if the right fence exists (aka the right fence value)
        """
        return self.homes_and_fences[h_i * 2 + 2]

    def __str__(self):
        ret = []
        for i in range(self.get_num_houses()):
            curr_home = self.get(0)
            # First house
            if i == 0:
                ret.append(curr_home.house.get_val())
                ret.append(curr_home.used_in_plan)
            # Non-first house
            else:
                ret.append([self.has_left_fence(i),
                            curr_home.house.get_val(),
                            curr_home.used_in_plan])
        return json.dumps(ret)
