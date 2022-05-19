from typing import List

from my_python.archive.a3.Homes import *


class Street:
    pool_indices = [[2, 6, 7], [0, 3, 7], [1, 6, 10]]
    park_indices = [3, 4, 5]

    @contract
    def __init__(self, st):
        """
            Initialize street object.

            :param st: Dictionary input representing a street
            :type st: valid_street
        """
        self.homes = Homes(st.get("homes"))
        self.parks = st.get("parks")
        self.pools = st.get("pools")

        ### Set street number we're on ###
        self.street_num = -1
        if self.homes.get_num_houses() == 10:
            self.street_num = 0  # first street
        elif self.homes.get_num_houses() == 11:
            self.street_num = 1  # second street
        else:
            self.street_num = 2  # third street

        ### Validate the pools ###
        pool_indices_for_curr_street = self.pool_indices[self.street_num]
        for i in range(3):
            if self.pools[i] is True:
                pot_house_w_pool_i = pool_indices_for_curr_street[i]
                # probably should have put used_in_plans field into House
                #   instead of creating the HomesElem class (were defining
                #   internal representation from json, which we realized
                #   could have been simplified)
                assert not self.homes.get(
                    pot_house_w_pool_i).get_house().get_is_bis(), "A house that is a bis cannot have a pool"
                assert self.homes.get(pot_house_w_pool_i).get_house().is_built(), "House that has a pool must be built"

        ### Validate the parks ###
        num_parks_for_curr_street = self.park_indices[self.street_num]
        assert 0 <= self.parks <= num_parks_for_curr_street, "Invalid number of parks for current street"

        ### Validate that num of parks is <= num of non-bis built homes ###
        assert self.get_parks() <= self.homes.get_num_non_bis_houses(), "num of parks is not <= num non-built homes"

    @contract
    def get_parks(self):
        """
            Get the number of parks in the street

            :type: None

            :return: A natural representing the number of parks
            :rtype: valid_parks
        """
        return self.parks

    @contract
    def get_pools(self):
        """
            Get the number of "active" pools in the street

            :type: None

            :return: List of Booleans representing which pools are "activated"
            :rtype: valid_pools
        """
        return self.pools

    def get_street_num(self) -> int:
        """
            Get index of which street this is (0, 1, 2)
            :return: 0, 1, 2
        """
        return self.street_num

    def get_num_built_houses(self) -> int:
        """
            Get the number of homes that are built (bis and non-bis) on the street
            :return: int representing the number of built (non-"blank") homes
        """
        count = 0
        for i in range(self.homes.get_num_houses()):
            curr_house = self.homes.get(i).get_house()
            if curr_house.is_built(): count += 1
        return count

    def return_literal(self):
        homes_val = [self.homes.get(0).house.get_val(), self.homes.get(0).used_in_plan]
        for i in range(self.homes.get_num_houses()):
            if i == 0: continue
            homes_val.append([
                self.homes.has_left_fence(i),
                self.homes.get(i).house.get_val(),
                self.homes.get(i).used_in_plan
            ])
        ret = {"homes": homes_val,
               "parks": self.parks,
               "pools": self.pools}
        return ret

    def get_num_built_pools(self) -> int:
        ret = 0
        for ea in self.pools:
            if ea is True: ret += 1
        return ret

    def get_num_bis(self) -> int:
        ret = 0
        for i in range(self.homes.get_num_houses()):
            if self.homes.get(i).house.get_is_bis(): ret += 1
        return ret

    def get_num_estates(self) -> List[int]:
        estate_count_dict = [None,0,0,0,0,0,0]
        counting_houses = False
        size_of_curr_house = 0
        for i in range(self.homes.get_num_houses()):
            if counting_houses is False and self.homes.has_left_fence(i) \
                    and self.homes.get(i).house.is_built():
                counting_houses = True
                size_of_curr_house = 1
            elif counting_houses is True and not self.homes.has_left_fence(i) \
                    and self.homes.get(i).house.is_built():
                size_of_curr_house += 1
            if counting_houses is True and self.homes.has_right_fence(i) \
                    and self.homes.get(i).house.is_built():
                counting_houses = False
                # To catch estates that are size >6
                try:
                    estate_count_dict[size_of_curr_house] += 1
                except IndexError:
                    pass
                size_of_curr_house = 0
            if not self.homes.get(i).house.is_built():
                counting_houses = False
                size_of_curr_house = 0
        return estate_count_dict

    def __str__(self):
        ret = {"homes": self.homes.__str__(),
               "parks": self.parks,
               "pools": self.pools}
        return json.dumps(ret)
