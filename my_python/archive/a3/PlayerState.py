from my_python.archive.a3.Street import *
from contracts import *

class PlayerState:
    valid_agent_values = [1, 2, 3, 4, 4, 4]

    @contract
    def __init__(self, ps):
        """
            Initialize LocalPlayer state from a valid player state dictionary.

            :param ps: The dictionary representing the input state
            :type ps: valid_player_state
        """
        self.agents = ps.get("agents")
        self.city_plan_score = ps.get("city-plan-score")
        ### Validate that refusals are natural numbers
        assert ps.get("refusals") >= 0 and isinstance(ps.get("refusals"), int) and not isinstance(ps.get("refusals"), bool), "refusals must be natural numbers"
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
        assert not isinstance(self.get_agents()[0], bool) and 0 <= self.get_agents()[0] <= self.valid_agent_values[0], "agent index 0 is not between [0,1]"
        assert not isinstance(self.get_agents()[1], bool) and 0 <= self.get_agents()[1] <= self.valid_agent_values[1], "agent index 1 is not between [0,2]"
        assert not isinstance(self.get_agents()[2], bool) and 0 <= self.get_agents()[2] <= self.valid_agent_values[2], "agent index 2 is not between [0,3]"
        assert not isinstance(self.get_agents()[3], bool) and 0 <= self.get_agents()[3] <= self.valid_agent_values[3], "agent index 3 is not between [0,4]"
        assert not isinstance(self.get_agents()[4], bool) and 0 <= self.get_agents()[4] <= self.valid_agent_values[4], "agent index 4 is not between [0,4]"
        assert not isinstance(self.get_agents()[5], bool) and 0 <= self.get_agents()[5] <= self.valid_agent_values[5], "agent index 5 is not between [0,4]"

        ### Validate refusals ###
        assert 0 <= self.get_refusals() <= 3, "refusals are not between [0,3]"

        ### Validate that temps are between [0, 11] ###
        assert 0 <= self.get_temps() <= 11, "temps are not between [0,11]"

        self.total_built_houses = 0
        self.total_claimed_city_plan_scores = 0

        ### Validate that the number of built homes is >= number of claimed city-plan's ###
        for street in self.get_streets():
            self.total_built_houses += street.get_num_built_houses()
        for nb in self.city_plan_score:
            if nb != "blank": self.total_claimed_city_plan_scores += 1
        # JK don't need this
        # assert self.total_built_houses >= self.total_claimed_city_plan_scores, "# of built homes is not >= # of claimed city plans"

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

    ### Validate that number of built homes is >= #fences + #pools + #temps + #agents + #parks + #claimed plans ###
    def validate_num_built_houses_geq_misc(self) -> bool:
        """
            Validate that the number of built homes is >= #fences + #pools + #temps + #agents + #parks + #claimed plans ###
            :return: true if the condition holds, AssertionError otherwise
        """
        misc_sum = 0
        misc_sum += self.get_total_built_fences() - 6   # -6 to account for first and last fence being built already
        for s in self.streets:
            misc_sum += s.get_pools().count(True)
            misc_sum += s.get_parks()
        misc_sum += self.temps
        misc_sum += sum(self.agents)
        misc_sum += self.total_claimed_city_plan_scores
        assert self.total_built_houses >= misc_sum, "number of built homes is less than #fences + #pools + #parks" \
                                                          " + #temps + #agents + #claimed plans"
        return True

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


def calc_score(ps: PlayerState, other_temps: List[int]) -> int:
    """
        Calculates the score of the current PlayerState.
        :return: integer score
    """

    def park_score(st_num: int, num_parks: int) -> int:
        parks_vals_s0 = [0, 2, 4, 10]
        parks_vals_s1 = [0, 2, 4, 6, 14]
        parks_vals_s2 = [0, 2, 4, 6, 8, 18]
        parks_vals = [parks_vals_s0, parks_vals_s1, parks_vals_s2]
        return parks_vals[st_num][num_parks]

    def calc_temp_score(curr_temp_count: int, other_temp_counts: List[int]) -> int:
        """Calculates the temp score one should get given a temp count and list of other players' temp counts"""
        if curr_temp_count == 0: return 0 # Special case
        temp_scores = [7, 4, 1]
        # Initialize total_temp_counts
        other_temp_counts.append(curr_temp_count)
        total_temp_counts = other_temp_counts
        # Remove duplicates from the list of all the temps
        no_dup_total_temp_counts = []
        [no_dup_total_temp_counts.append(el) for el in total_temp_counts if el not in no_dup_total_temp_counts]
        # See which "place" the curr_temp_count slots in at
        no_dup_total_temp_counts = sorted(no_dup_total_temp_counts, reverse=True)
        place = (len(no_dup_total_temp_counts)) - 1
        for i in range(len(no_dup_total_temp_counts)):
            if no_dup_total_temp_counts[i] == curr_temp_count: place = i
        # Return the corresponding temp score based on the place
        try:
            return temp_scores[place]
        except IndexError:
            return 0

    def calc_agent_score(agents_ind: int, agents_val: int) -> int:
        """Calculates the agent score for a given agent index and agent value."""
        agent_scores = [
            [1,3],
            [2,3,4],
            [3,4,5,6],
            [4,5,6,7,8],
            [5,6,7,8,10],
            [6,7,8,10,12]
        ]
        return agent_scores[agents_ind][agents_val]

    def calc_bis_penalty(num_built_bis: int) -> int:
        bis_penalties = [0, 1, 3, 6, 9, 12, 16, 20, 24, 28]
        return bis_penalties[num_built_bis]

    def count_total_player_estates(ps: PlayerState) -> List:
        """Returns a direct-addressing dictionary of format [None, int, int, int, int, int, int]
        corresponding to number of index-size estates."""
        total_estates_dict = [None, 0,0,0,0,0,0]
        for st in ps.streets:
            curr_street_estate_dict = st.get_num_estates()
            for i in range(7):
                if i != 0:
                    total_estates_dict[i] = total_estates_dict[i] + curr_street_estate_dict[i]
        return total_estates_dict

    rscore = 0
    ##### Add up the claimed city plan scores
    for nb in ps.city_plan_score:
        if nb != "blank": rscore += nb
    # print('claimed city plan scores', rscore, '--------CHECK---------')
    fooo = rscore
    ##### Add up the parks scores
    for i in range(3):
        curr_street = ps.streets[i]
        rscore += park_score(i, curr_street.parks)
    # print('park scores', rscore - fooo, '--------CHECK---------')
    fooo = rscore
    ##### Add up the pools scores
    total_built_pools = 0
    for ea in ps.streets:
         total_built_pools += ea.get_num_built_pools()
    rscore += [0,3,6,9,13,17,21,26,31,36][total_built_pools]
    # print('pool score', rscore - fooo)
    foooo = rscore
    ##### Add up the temps score
    rscore += calc_temp_score(ps.temps, other_temps)
    ##### Add up the agent scores
    agent_score_multipliers = []
    for i in range(len(ps.agents)):
        agent_score_multipliers.append(calc_agent_score(i, ps.agents[i]))
    # Add (score for size-n estate)*(num size-n estates) for each size-n estate
    total_player_estates = count_total_player_estates(ps)
    foo = 0
    for i in range(6):
        rscore += agent_score_multipliers[i] * total_player_estates[i + 1]
        foo += agent_score_multipliers[i] * total_player_estates[i + 1]

    ##### Subtract bis penalty
    total_bis = 0
    # Iterate through each street and add the bis's to the total count
    for st in ps.streets:
        total_bis += st.get_num_bis()
    rscore -= calc_bis_penalty(total_bis)
    ##### Subtract the refusals penalty
    refusal_scores = [0,0,3,5]
    rscore -= refusal_scores[ps.refusals]

    return rscore



