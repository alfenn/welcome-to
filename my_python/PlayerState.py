import json
import sys
from collections import Counter

sys.path.append('../../')
from my_python.House import House
from my_python.contracts import playerstate_contract
from my_python.Street import Street
from my_python.exceptions import InvalidPlayerState
from my_python.Same import same_or_get_first

class PlayerState:
    def __init__(self, **kwargs):
        self.agents = []
        self.city_plan_score = []
        self.refusals = 0
        self.streets = []
        self.temps = 0
        inp_ps = kwargs.get("inp_ps", {"agents": [0, 0, 0, 0, 0, 0],"city-plan-score": ["blank", "blank", "blank"],"refusals": 0,"streets": [{"homes": ["blank", False,[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False]],"parks": 0,"pools": [False, False, False]},{"homes": ["blank", False,[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False]],"parks": 0,"pools": [False, False, False]},{"homes": ["blank", False,[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False],[False, "blank", False]],"parks": 0,"pools": [False, False, False]}],"temps": 0})
        if not playerstate_contract(inp_ps): raise InvalidPlayerState("Breaks PlayerState contract")
        ### Normal processing of standard inputs.
        self.agents = inp_ps["agents"]
        self.city_plan_score = inp_ps["city-plan-score"]
        self.refusals = inp_ps["refusals"]
        self.temps = inp_ps["temps"]

        for i in range(3):
            self.streets.append(Street(inp_street=inp_ps["streets"][i]))

        ## Check the number of roundabouts that were played
        self._check_num_roundabouts()

        ### If class fields are specified, set them directly
        try:
            self.agents = kwargs["agents"]
            self.city_plan_score = kwargs["city_plan_score"]
            self.refusals = kwargs["refusals"]
            self.streets = kwargs["streets"]
            self.temps = kwargs["temps"]
        except KeyError:
            pass

    def get_total_num_roundabouts(self) -> int:
        total_roundabouts = 0
        for curr_street in self.streets:
            total_roundabouts += curr_street.get_num_roundabouts()
        return total_roundabouts

    def _check_num_roundabouts(self) -> None:
        if self.get_total_num_roundabouts() > 2:
            raise InvalidPlayerState("Number of roundabouts cannot exceed 2.")

    def get_total_non_bis_houses(self) -> int:
        num_non_bis_houses_i = 0
        for i in range(3):
            curr_street: Street = self.streets[i]
            for i in range(len(curr_street.homes)):
                curr_house: House = curr_street.homes[i]
                if curr_house.is_built and not curr_house.is_bis: num_non_bis_houses_i += 1
        return num_non_bis_houses_i

    def get_total_built_houses(self) -> int:
        num_built_houses = 0
        for curr_street in self.streets:
            for curr_house in curr_street.homes:
                if curr_house.is_built:
                    num_built_houses += 1
        return num_built_houses

    def get_total_bis_houses(self) -> int:
        return self.get_total_built_houses() - self.get_total_non_bis_houses()

    def no_space(self) -> bool:
        """Returns true if there is no space to build any new houses, false if space exists"""
        return (self.get_total_built_houses() + self.get_total_num_roundabouts()) == 33

    def get_num_played_effects(self) -> int:
        num_agents_i = 0
        num_claimed_plans_i = 0
        num_bis_i = 0
        num_parks_i = 0
        num_pools_i = 0
        num_temps_i = self.temps
        num_built_fences_i = -6

        for i in range(3):
            curr_street: Street = self.streets[i]
            for j in range(len(curr_street.homes)):
                curr_house = curr_street.homes[j]
                if j == 0:
                    if curr_house.l_fence.exists: num_built_fences_i += 1
                if curr_house.r_fence.exists: num_built_fences_i += 1
                if curr_house.is_bis: num_bis_i += 1
            num_parks_i += curr_street.parks
            for i in range(3):
                if curr_street.pools[i]: num_pools_i += 1
        for i in range(6):
            num_agents_i += self.agents[i]
        for i in range(3):
            if self.city_plan_score[i] != "blank": num_claimed_plans_i += 1
        return num_agents_i + num_claimed_plans_i + num_bis_i + num_parks_i + num_pools_i + num_temps_i + num_built_fences_i
        # if not ((num_agents_i + num_claimed_plans_i + num_bis_i + num_parks_i + num_pools_i + num_temps_i + num_built_fences_i) <= self.help_total_non_bis_houses()): raise InvalidPlayerState("Number of effects is > number of non-bis houses")
        # if not ((num_built_fences_i) <= self._help_total_non_bis_houses()): raise InvalidPlayerState("Number of effects is > number of non-bis houses")

    def __eq__(self, other):
        # Check: agents
        if self.agents != other.agents: return False
        # Check: city_plan_score
        if self.city_plan_score != other.city_plan_score: return False
        # Check: refusals
        if self.refusals != other.refusals: return False
        # Check: temps
        if self.temps != other.temps: return False
        # Check: streets
        for i in range(3):
            if self.streets[i] != other.streets[i]: return False
        return True

    def __sub__(self, other):
        temp_agents = []
        for i in range(6):
            temp_agents.append(same_or_get_first(self.agents[i], other.agents[i]))
        temp_city_plan_score = []
        for i in range(3):
            temp_city_plan_score.append(same_or_get_first(self.city_plan_score[i], other.city_plan_score[i]))
        temp_refusals = same_or_get_first(self.refusals, other.refusals)
        temp_streets = []
        for i in range(3):
            temp_streets.append(self.streets[i] - other.streets[i])
        temp_temps = same_or_get_first(self.temps, other.temps)
        return PlayerState(agents=temp_agents, city_plan_score=temp_city_plan_score, refusals=temp_refusals, streets=temp_streets, temps=temp_temps)

    def __str__(self):
        ret = {"agents": self.agents,
               "city-plan-score": self.city_plan_score,
               "refusals": self.refusals,
               "streets": [
                   self.streets[0].return_literal(),
                   self.streets[1].return_literal(),
                   self.streets[2].return_literal()
               ],
               "temps": self.temps
            }
        return json.dumps(ret)

    def return_literal(self):
        ret = {"agents": self.agents,
               "city-plan-score": self.city_plan_score,
               "refusals": self.refusals,
               "streets": [
                   self.streets[0].return_literal(),
                   self.streets[1].return_literal(),
                   self.streets[2].return_literal()
               ],
               "temps": self.temps
               }
        return ret
