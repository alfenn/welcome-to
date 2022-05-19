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
        inp_street = kwargs.get("inp_street", {"houses": ["blank", False,[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False] ],"parks": 0,"pools": [False, False, False]})
        if not street_contract(inp_street): raise InvalidPlayerState("Breaks House contract")
        ### Normal processing of standard inputs.
        self.houses = []
        self.parks = 0
        self.pools = [False, False, False]

        for i in range(len(inp_street["houses"])):
            if i == 0:
                # Deal with the first House. Initialize right fence with placeholder.
                self.houses.append(House(inp_house=inp_street["houses"][0],
                                         used_in_plan=inp_street["houses"][1],
                                         l_fence=Fence(True),
                                         r_fence=Fence(True)))
            # If `i` is not the first House...
            if i > 1:
                # All these houses follow schema: [ fence-or-not, house, used-in-plan ]
                curr_house = inp_street["houses"][i]
                temp_l_fence = Fence(inp_street["houses"][i][0])
                houses_ind = i - 1                                          # We're off by 1 bc we skip ["houses"][1]
                self.houses[houses_ind - 1].r_fence = temp_l_fence          # Link right fence of prev House...
                self.houses.append(House(inp_house=curr_house[1],
                                         used_in_plan=curr_house[2],
                                         l_fence=temp_l_fence,              # ... to left fence of curr House.
                                         r_fence=Fence(True)))              # Use placeholder for right fence.
        self.parks = inp_street["parks"]
        self.pools = inp_street["pools"]
        # Check: boolean elements of pools are actually built at corresponding .houses index
        ##  Note: We are not putting this in "street_contract" since this check involves initializing a
        ##      Street object, which would create a circular import.
        self._check_pools()
        # Check: .parks has an appropriate upper bound determined by the length of the street.
        ##  Note: We are not putting this in the "street_contract" for the same reason as above--
        ##      we need fields across the entire Street object.
        self._check_parks()
        ## ===================== If class fields are specified, set them directly ====================
        try:
            self.houses = kwargs["houses"]
            self.parks = kwargs["parks"]
            self.pools = kwargs["pools"]
        except KeyError:
            pass

    def _street_ind(self) -> int:
        """Maps street length to a street index according to (10,0), (11,1), (12,2)."""
        return len(self.houses) % 10

    def _check_pools(self) -> None:
        pool_locations = [[2, 6, 7], [0, 3, 7], [1, 6, 10]]
        pool_locations_curr_st = pool_locations[self._street_ind()]
        # Iterate over "pools"
        for i in range(3):
            # If there is a True, check the corresponding .houses ind
            if self.pools[i] is True:
                # If it is not built return False
                if not self.houses[
                    pool_locations_curr_st[i]
                ].is_built:
                    raise InvalidPlayerState("House for corresponding pool value is not built.")
                # Built houses can not be "bis"
                else:
                    if self.houses[
                        pool_locations_curr_st[i]
                    ].is_bis:
                        raise InvalidPlayerState("House for corresponding pool value is a \"bis\".")

    def _check_parks(self) -> None:
        park_max = [3, 4, 5]
        park_max_curr_st = park_max[self._street_ind()]
        if not self.parks <= park_max_curr_st:
            raise InvalidPlayerState("Parks value is not less than max for the given street length.")

    def __sub__(self, other):
        if len(self.houses) != len(other.houses): ValueError("Streets have different numbers of houses.")
        temp_houses = []
        for i in range(len(self.houses)):
            temp_houses.append(self.houses[i] - other.houses[i])
        temp_parks = same_or_get_first(self.parks, other.parks)
        temp_pools = []
        for i in range(3):
            temp_pools.append(same_or_get_first(self.pools[i], other.pools[i]))
        return Street(houses=temp_houses, parks=temp_parks, pools=temp_pools)

    def __eq__(self, other):
        # Check: .houses length
        if len(self.houses) != len(other.houses): return False
        # Check: each House
        for i in range(len(self.houses)):
            if self.houses[i] != other.houses[i]: return False
        # Check: parks
        if self.parks != other.parks: return False
        if self.pools != other.pools: return False
        return True
