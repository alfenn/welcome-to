import sys
from typing import List
from collections import Counter

sys.path.append('../../../')
from my_python.PlayerState import PlayerState
from my_python.Street import Street
from my_python.House import House


def calc_score(ps: PlayerState, other_temps: List[int]) -> int:
    """
    Calculates the score of a player, given a player and a list of the
    temp counts of the other players
    """

    def get_street_park_score(street_index: int, num_parks: int) -> int:
        """
        Returns the park bonus for a street, given the index of the street
        and the number of parks built for that street
        """
        park_scores = [[0, 2, 4, 10],
                      [0, 2, 4, 6, 14],
                      [0, 2, 4, 6, 8, 18]]
        return park_scores[street_index][num_parks]

    def get_pool_score(num_pools: int) -> int:
        """
        Returns the pool bonus, given the total number of pools that were built
        """
        pool_scores = [0, 3, 6, 9, 13, 17, 21, 26, 31, 36]
        return pool_scores[num_pools]

    def get_temp_score(ps_temp_score: int, other_temp_scores: List[int]) -> int:
        """
        Returns the player's temp bonus, given the player's temp score and a
        list of the other players' temp scores
        """
        if ps_temp_score == 0:
            return 0     # special case
        temp_scores = [7, 4, 1]
        #######
        ## Figure out the rank of ps_temp_score with friendly ties
        #######
        # Create a list of all players' temp scores without duplicates
        other_temp_scores.append(ps_temp_score)
        all_temp_scores = list(set(other_temp_scores))
        all_temp_scores.sort(reverse=True)  # sort in descending order (largest score first)
        rank = len(all_temp_scores) - 1     # set initial value of rank to be the highest value
        for i in range(len(all_temp_scores)):
            if all_temp_scores[i] == ps_temp_score:
                rank = i
        # If rank is outside the top 3, return temp_score=0
        try:
            return temp_scores[rank]
        except IndexError:
            return 0

    def get_agent_score(estate_size: int, agents_played: int) -> int:
        """
        Returns the agent bonus for an estate size, given the estate size
        and the number of agents played for that estate size
        """
        estate_size -= 1
        agent_scores = [
            [1, 3],
            [2, 3, 4],
            [3, 4, 5, 6],
            [4, 5, 6, 7, 8],
            [5, 6, 7, 8, 10],
            [6, 7, 8, 10, 12]
        ]
        return agent_scores[estate_size][agents_played]

    def get_bis_penalty(num_bis: int) -> int:
        """
        Returns the bis penalty, given the number of bis's that were built
        """
        bis_penalties = [0, 1, 3, 6, 9, 12, 16, 20, 24, 28]
        # If more than 9 bis were built, return penalty of 28
        try:
            return bis_penalties[num_bis]
        except IndexError:
            return 28

    def get_refusals_penalty(num_refusals: int) -> int:
        """
        Returns the refusals penalty, given the number of refusals used
        """
        refusals_scores = [0,0,3,5]
        return refusals_scores[num_refusals]

    def get_roundabouts_penalty(num_roundabouts: int) -> int:
        roundabout_penalties = [0, 3, 5]
        return roundabout_penalties[num_roundabouts]

    def count_total_player_estates(ps: PlayerState) -> Counter:
        """
        Returns a multiset() storing the count of each size estate
        """
        estates: Counter = Counter()
        # Loop through each street
        for i in range(3):
            curr_street: Street = ps.streets[i]
            counting_houses = False
            curr_estate_start_end = [None, None]
            # Loop through each house on the street
            for j in range(len(curr_street.homes)):
                curr_house: House = curr_street.homes[j]
                # Start counting houses once we encounter a built house with a left fence
                if not counting_houses and curr_house.l_fence.exists\
                                       and curr_house.is_built:
                    counting_houses = True
                    curr_estate_start_end[0] = j
                # Stop counting when...
                #   1. the current house has a right fence
                #       a. in which case we save `j` as the end of the estate
                #   2. the current house is "blank"
                #       a. in which case we save `j-1` as the end of the estate
                if counting_houses:
                    if curr_house.r_fence.exists and curr_house.is_built:
                        counting_houses = False
                        curr_estate_start_end[1] = j
                    if not curr_house.is_built:
                        counting_houses = False
                        curr_estate_start_end[1] = j-1
                # Check if we should be adding the current estate
                if (not counting_houses) and (curr_estate_start_end != [None, None]):   # we aren't counting, and we have an estate saved
                    # Only add if the estate has a left and right fence
                    start_house: House = ps.streets[i].homes[curr_estate_start_end[0]]
                    end_house: House = ps.streets[i].homes[curr_estate_start_end[1]]
                    if start_house.l_fence.exists and end_house.r_fence.exists:
                        estates.update([curr_estate_start_end[1]-curr_estate_start_end[0] + 1])
                    curr_estate_start_end = [None, None]
        return estates


    score = 0
    # Add up the claimed city plan scores
    for nb in ps.city_plan_score:
        if nb != "blank":
            score += nb
    # Add up the parks scores
    for i in range(3):
        score += get_street_park_score(i, ps.streets[i].parks)
    # Add up the pools scores
    built_pools = 0
    for curr_street in ps.streets:
        built_pools += curr_street.pools.count(True)
    score += get_pool_score(built_pools)
    # Add up the temp scores
    score += get_temp_score(ps.temps, other_temps)
    # Add up the agents scores
    #   Calculate the agent multipliers for each size estate
    agent_scores = [1,2,3,4,5,6]
    for i in range(len(ps.agents)):
        agent_scores[i] = get_agent_score(i+1, ps.agents[i])
    #   Add the corresponding estate score to the total score
    player_estates = count_total_player_estates(ps)
    for i in range(6):
        score += agent_scores[i] * player_estates[i + 1]    # agent_scores[i] = score for size i+1 estate
                                                            # player_estates[n] = number of size n estates
    # Subtract the bis penalty
    num_bis = ps.get_total_bis_houses()
    score -= get_bis_penalty(num_bis)
    # Subtract the refusals penalty
    score -= get_refusals_penalty(ps.refusals)
    # Subtract the roundabout penalty
    score -= get_roundabouts_penalty(ps.get_total_num_roundabouts())

    return score
