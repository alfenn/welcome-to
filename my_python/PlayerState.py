import sys

from my_python.House import House

sys.path.append('../../')
from my_python.contracts import player_contract
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
        if not player_contract(inp_ps): raise InvalidPlayerState("Breaks PlayerState contract")
        ### Normal processing of standard inputs.
        self.agents = inp_ps["agents"]
        self.city_plan_score = inp_ps["city-plan-score"]
        self.refusals = inp_ps["refusals"]
        self.temps = inp_ps["temps"]

        for i in range(3):
            self.streets.append(Street(inp_street=inp_ps["streets"][i]))

        ## Check: number of used effects <= built houses
        self._check_effects_vs_built_houses()

        ### If class fields are specified, set them directly
        try:
            self.agents = kwargs["agents"]
            self.city_plan_score = kwargs["city_plan_score"]
            self.refusals = kwargs["refusals"]
            self.streets = kwargs["streets"]
            self.temps = kwargs["temps"]
        except KeyError:
            pass

    def _check_effects_vs_built_houses(self) -> None:
        num_fences_i = 0
        for i in range(3):
            curr_street: Street = self.streets[i]
            for j in range(len(curr_street.homes)):
                curr_house = curr_street.homes[j]
                if j == 0:
                    if curr_house.l_fence.exists: num_fences_i += 1
                if curr_house.r_fence.exists: num_fences_i += 1
        if not num_fences_i <= self._help_total_non_bis_houses(): InvalidPlayerState("Number of fences is > number of non-bis houses")

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
