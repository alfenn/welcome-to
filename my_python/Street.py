import sys
sys.path.append("../../")
from my_python.exceptions import InvalidPlayerState
from my_python.contracts import street_contract
from my_python.House import House
from my_python.Fence import Fence
from my_python.Same import same_or_get_first

class Street:
    # def __init__(self, inp_street):
    def __init__(self, **kwargs):
        ## ===================== Standard input ====================
        ### If this argument is not specified, initialize values to a valid
        ### placeholder. This is to pass the validators in the case that we
        ### are setting the class fields directly.
        inp_street = kwargs.get("inp_street", {"homes": ["blank", False,[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False] ],"parks": 0,"pools": [False, False, False]})
        if not street_contract(inp_street): raise InvalidPlayerState("Breaks House contract")
        ### Normal processing of standard inputs.
        self.homes = []
        self.parks = 0
        self.pools = [False, False, False]

        for i in range(len(inp_street["homes"])):
            if i == 0:
                # Deal with the first House. Initialize right fence with placeholder.
                self.homes.append(House(inp_house=inp_street["homes"][0],
                                        used_in_plan=inp_street["homes"][1],
                                        l_fence=Fence(True),
                                        r_fence=Fence(True)))
            # If `i` is not the first House...
            if i >= 2:
                # All these homes follow schema: [ fence-or-not, house, used-in-plan ]
                curr_house = inp_street["homes"][i]
                temp_l_fence = Fence(inp_street["homes"][i][0])
                houses_ind = i - 1                                          # We're off by 1 bc we skip ["homes"][1]
                self.homes[houses_ind - 1].r_fence = temp_l_fence          # Link right fence of prev House...
                self.homes.append(House(inp_house=curr_house[1],
                                        used_in_plan=curr_house[2],
                                        l_fence=temp_l_fence,  # ... to left fence of curr House.
                                        r_fence=Fence(True)))              # Use placeholder for right fence.
        self.parks = inp_street["parks"]
        self.pools = inp_street["pools"]
        # Check: boolean elements of pools are actually built at corresponding .homes index
        ##  Note: We are not putting this in "street_contract" since this check involves initializing a
        ##      Street object, which would create a circular import.
        self._check_pools()
        # Check: .parks has an appropriate upper bound determined by the length of the street.
        ##  Note: We are not putting this in the "street_contract" for the same reason as above--
        ##      we need fields across the entire Street object.
        self._check_parks()
        ## Check: bis
        self._check_bis()
        ## Check: no fences between bis's
        self._check_fence_btwn_same_num()
        ## Check: ascending order
        self._check_ascending_order()
        ## Check: make sure that the num of parks is <= built houses
        self._parks_built_houses()
        ## ===================== If class fields are specified, set them directly ====================
        try:
            self.homes = kwargs["homes"]
            self.parks = kwargs["parks"]
            self.pools = kwargs["pools"]
        except KeyError:
            pass

    def _street_ind(self) -> int:
        """Maps street length to a street index according to (10,0), (11,1), (12,2)."""
        return len(self.homes) % 10

    def _check_pools(self) -> None:
        pool_locations = [[2, 6, 7], [0, 3, 7], [1, 6, 10]]
        pool_locations_curr_st = pool_locations[self._street_ind()]
        # Iterate over "pools"
        for i in range(3):
            # If there is a True, check the corresponding .homes ind
            if self.pools[i] is True:
                # If it is not built return False
                if not self.homes[
                    pool_locations_curr_st[i]
                ].is_built:
                    raise InvalidPlayerState("House for corresponding pool value is not built.")
                # Built homes can not be "bis"
                else:
                    if self.homes[
                        pool_locations_curr_st[i]
                    ].is_bis:
                        raise InvalidPlayerState("House for corresponding pool value is a \"bis\".")

    def _check_parks(self) -> None:
        park_max = [3, 4, 5]
        park_max_curr_st = park_max[self._street_ind()]
        if not self.parks <= park_max_curr_st:
            raise InvalidPlayerState("Parks value is not less than max for the given street length.")

    def _check_bis(self) -> None:
        bis_counter = 0
        curr_not_bis_house = None

        for i in range(len(self.homes)):
            curr_house: House = self.homes[i]
            if i > 0:
                curr_house_bef: House = self.homes[i-1]
            if i < (len(self.homes) - 1):
                curr_house_aft: House = self.homes[i+1]

            if not curr_house.is_bis and curr_house.is_built:
                curr_not_bis_house = curr_house.num
                if (0 < i <= (len(self.homes) - 1)) and (curr_not_bis_house == curr_house_bef.num or curr_not_bis_house == curr_house_aft.num) and bis_counter > 0:
                    bis_counter = 0
                continue

            if curr_house.is_bis and i == 0:
                if curr_house.num == curr_house_aft.num:
                    if curr_house_aft.is_bis:
                        bis_counter += 1
                    continue
                else:
                    raise InvalidPlayerState("Current bis'd house does not match the house before or after")

            if curr_house.is_bis:
                if curr_house.num == curr_house_bef.num:
                    if curr_house_bef.is_bis:
                        if curr_house.num == curr_not_bis_house:
                            bis_counter = 0
                        else:
                            bis_counter += 1
                        continue
                    continue
                elif curr_house.num == curr_house_aft.num:
                    if curr_house_aft.is_bis:
                        if curr_house.num == curr_not_bis_house:
                            bis_counter = 0
                        else:
                            bis_counter += 1
                        continue
                    continue

                else:
                    raise InvalidPlayerState("Current bis'd house does not match the house before or after")

            if curr_house.is_bis and i == (len(self.homes) - 1):
                if curr_house.num == curr_house_bef.num:
                    if curr_house_bef.is_bis:
                        if curr_house.num == curr_not_bis_house:
                            bis_counter = 0
                        else:
                            bis_counter += 1
                    continue

                else:
                    raise InvalidPlayerState("Current bis'd house does not match the house before or after")

        if bis_counter > 0:
            raise InvalidPlayerState("All homes cannot be bis'd")

    def _check_fence_btwn_same_num(self) -> None:
        i = 1
        while i < len(self.homes):
            house1: House = self.homes[i]
            house2: House = self.homes[i-1]
            if (house1.num == house2.num
                    and house1.is_built and house2.is_built):
                if house2.r_fence.exists:
                    raise InvalidPlayerState("Cannot be a fence between houses of the same num")
            i += 1

    def _check_ascending_order(self) -> None:
        built_houses = []
        for i in range(len(self.homes)):
            curr_house = self.homes[i]
            if curr_house.is_built:
                built_houses.append(curr_house)
        for i in range(len(built_houses) - 1):
            i += 1
            house1 = built_houses[i]
            house2 = built_houses[i-1]
            if house1.num < house2.num: raise InvalidPlayerState("Homes are not in ascending order")

    def _check_no_dups(self) -> None:
        built_non_bis_houses = []
        for i in range(len(self.homes)):
            curr_house = self.homes[i]
            if curr_house.is_built and not curr_house.is_bis:
                for j in range(len(built_non_bis_houses)):
                    if curr_house == built_non_bis_houses[j]: raise InvalidPlayerState("Homes cannot have any duplicate non-bis houses")
                    built_non_bis_houses.append(curr_house)

    def _help_total_non_bis_houses(self) -> int:
        num_non_bis_houses_i = 0
        for i in range(len(self.homes)):
            curr_house: House = self.homes[i]
            if curr_house.is_built and not curr_house.is_bis: num_non_bis_houses_i += 1
        return num_non_bis_houses_i

    def _parks_built_houses(self) -> None:
        # "Landscaper: Parks must be crossed off on the same street that the house number is written."
        if not (self._help_total_non_bis_houses() >= self.parks): raise InvalidPlayerState("Number of non-bis built houses must be >= number of parks on street")

    def __sub__(self, other):
        if len(self.homes) != len(other.homes): ValueError("Streets have different numbers of homes.")
        temp_homes = []
        for i in range(len(self.homes)):
            temp_homes.append(self.homes[i] - other.homes[i])
        temp_parks = same_or_get_first(self.parks, other.parks)
        temp_pools = []
        for i in range(3):
            temp_pools.append(same_or_get_first(self.pools[i], other.pools[i]))
        return Street(homes=temp_homes, parks=temp_parks, pools=temp_pools)

    def __eq__(self, other):
        # Check: .homes length
        if len(self.homes) != len(other.homes): return False
        # Check: each House
        for i in range(len(self.homes)):
            if self.homes[i] != other.homes[i]: return False
        # Check: parks
        if self.parks != other.parks: return False
        if self.pools != other.pools: return False
        return True
