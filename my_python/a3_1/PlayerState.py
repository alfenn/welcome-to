from typing import List
from my_python.a3_1.Street import *

class PlayerState:
    valid_agent_values = [1, 2, 3, 4, 4, 4]

    @contract
    def __init__(self, ps):
        """
            Initialize Player state from a valid player state dictionary.

            :param ps: The dictionary representing the input state
            :type ps: valid_player_state
        """
        self.agents = ps.get("agents")
        self.city_plan_score = ps.get("city-plan-score")
        self.refusals = ps.get("refusals")
        self.streets = []
        for elem in ps.get("streets"):
            self.streets.append(Street(elem))
        self.temps = ps.get("temps")

        ### Validate that street[0] is len 10, ... , street[2] is len 12
        assert self.get_streets()[0].get_street_num() == 0, "index 0 street is not len 10"
        assert self.get_streets()[1].get_street_num() == 1, "index 1 street is not len 11"
        assert self.get_streets()[2].get_street_num() == 2, "index 2 is not len 12"

        ### Validate that agent[0] is between [0, valid_agent_values[0]]... ###
        assert len(self.get_agents()) == 6, "length of agents array is not 6"
        assert 0 <= self.get_agents()[0] <= self.valid_agent_values[0], "agent index 0 is not between [0,1]"
        assert 0 <= self.get_agents()[1] <= self.valid_agent_values[1], "agent index 1 is not between [0,2]"
        assert 0 <= self.get_agents()[2] <= self.valid_agent_values[2], "agent index 2 is not between [0,3]"
        assert 0 <= self.get_agents()[3] <= self.valid_agent_values[3], "agent index 3 is not between [0,4]"
        assert 0 <= self.get_agents()[4] <= self.valid_agent_values[4], "agent index 4 is not between [0,4]"
        assert 0 <= self.get_agents()[5] <= self.valid_agent_values[5], "agent index 5 is not between [0,4]"

        ### Validate refusals ###
        assert 0 <= self.get_refusals() <= 3, "refusals are not between [0,3]"

        ### Validate that temps are between [0, 11] ###
        assert 0 <= self.get_temps() <= 11, "temps are not between [0,11]"

        self.count_total_built_houses = 0
        self.count_total_claimed_city_plan_scores = 0

        ### Validate that the number of built houses is >= number of claimed city-plan's ###
        for street in self.get_streets():
            self.count_total_built_houses += street.get_num_built_houses()
        for nb in self.city_plan_score:
            if nb != "blank": self.count_total_claimed_city_plan_scores += 1
        assert self.count_total_built_houses >= self.count_total_claimed_city_plan_scores, "# of built houses is not >= # of claimed city plans"

        ### Validate city plan scores are >= 0 if not "blank" ###
        for i in range(len(self.city_plan_score)):
            curr_city_plan_score = self.city_plan_score[i]
            if curr_city_plan_score != "blank":
                assert curr_city_plan_score >= 0, "index " + i + " city plan score is non-blank and not >= 0"

        ### Comment this out when unit testing ###
        # self.validate_num_built_houses_geq_misc()


    @contract
    def get_agents(self):
        """
            Gets the 'agents' field of the player state.

            :type: None

            :return: List representing agents
            :rtype: valid_agents
        """
        return self.agents

    def get_city_plan_score(self) -> List:
        """
            Gets the 'city_plan_score' of the player state.

            :type: None

            :return: List representing the city_plan_scores
        """
        return self.city_plan_score

    @contract
    def get_refusals(self):
        """
            Gets the 'refusals' of the player state.

            :type: None

            :return: Natural
            :rtype: valid_refusals
        """
        return self.refusals

    def get_streets(self) -> List[Street]:
        """
            Gets the 'streets' of the player state.

            :type: None
            :return: List representing the number of streets
        """
        return self.streets

    @contract
    def get_temps(self):
        """
            Returns the 'temps' field of the player state.

            :type: None

            :return: Number representing the number of temps a player has used.
            :rtype: valid_temps
        """
        return self.temps

    def get_total_built_fences(self) -> int:
        """
            Returns the total number of built fences.

            :type: None
            :return: int representing the total number of built fences.
        """
        count = 0
        for st in self.streets:
            count += st.homes.get_num_built_fences()
        return count

    ### Validate that number of built houses is >= #fences + #pools + #temps + #agents + #parks + #claimed plans ###
    def validate_num_built_houses_geq_misc(self) -> bool:
        """
            Validate that the number of built houses is >= #fences + #pools + #temps + #agents + #parks + #claimed plans ###
            :return: true if the condition holds, AssertionError otherwise
        """
        misc_sum = 0
        misc_sum += self.get_total_built_fences() - 6   # -6 to account for first and last fence being built already
        for s in self.streets:
            misc_sum += s.get_pools().count(True)
            misc_sum += s.get_parks()
        misc_sum += self.temps
        misc_sum += sum(self.agents)
        misc_sum += self.count_total_claimed_city_plan_scores
        assert self.count_total_built_houses >= misc_sum, "number of built houses is less than #fences + #pools + #parks" \
                                                          " + #temps + #agents + #claimed plans"
        return True

    # def validate_fences_geq_num_city_plans_claimed(self) -> bool:
    #     """
    #         Validate that the number of fences is at least the number of claimed plans + 1
    #         :return: true if the condition holds, AssertionError otherwise
    #     """
    #     assert self.get_total_built_fences() >= self.count_total_claimed_city_plan_scores + 1, "total number of " \
    #                                                                                            "fences is not geq num " \
    #                                                                                            "claimed city plans + 1"
    #     return True