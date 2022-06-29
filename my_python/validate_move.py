import json
import sys
from collections import Counter     # https://docs.python.org/3/library/collections.html#collections.Counter

sys.path.append('../../')
from my_python.PlayerState import PlayerState
from my_python.GameState import GameState
from my_python.Street import Street
from my_python.House import House
from my_python.exceptions import InvalidMove
from my_python.GenValidMove import GenValidMove


# Put this as helper that takes ps1 and ps2 because of the assumption that ps1 is correct:
#   https://piazza.com/class/l0wlxndauhb4xv?cid=163
def get_estates(ps1: PlayerState, ps2: PlayerState) -> Counter:
    """
    Returns a set such that it holds all the estates that are uip.
    """
    estates: Counter = Counter()
    # Loop through each street
    for i in range(3):
        curr_street: Street = ps2.streets[i]
        counting_houses = False
        curr_estate_start_end = [None, None]
        for j in range(len(curr_street.homes)):
            if ps1.streets[i].homes[j] != ps2.streets[i].homes[j] or counting_houses:
                curr_house: House = curr_street.homes[j]
                # 09_21 edge case: house becomes uip but isn't a valid estate
                #   Perhaps a more elegant way to do this might be:
                #       1. Anytime there's a used in plan house, we add it to the counter
                #       2. Consider adding it to set() every time we add a house to the estate
                #       3. Before we add it to set(), we check the beginning and end to make sure it's bounded by fences
                #   Current way of doing it which doesn't account for this edge case:
                #       1. Only start counting houses if the current house we're on is a valid house to be uip.
                #       2. (We're essentially ignoring all uip houses that are invalid, when we should be error-ing)

                # Start counting houses once we encounter a newly used-in-plan house
                if not counting_houses and curr_house.used_in_plan:
                    counting_houses = True
                    curr_estate_start_end[0] = j
                # Stop counting when either the current house has a right fence, or the house is blank
                #   Cases are:
                #       1. Must be currently counting houses and either...
                #           a. the current house is uip and has a right fence or
                #           (b. the current house is not used in plan or
                #           c. the current house is "blank" for us to stop counting)
                if counting_houses:
                    if curr_house.used_in_plan and curr_house.r_fence.exists:
                        counting_houses = False
                        curr_estate_start_end[1] = j    # set end house to j
                    if (not curr_house.used_in_plan) or (not curr_house.is_built):
                        counting_houses = False
                        curr_estate_start_end[1] = j-1  # set end house to j-1 bc current house isn't part of estate
                # Check if we should be adding the current estate, or if we should error
                if (not counting_houses) and (curr_estate_start_end != [None, None]):   # not counting and we have
                                                                                            # an estate saved.
                    # If the estate doesn't have a left and right fence then error
                    start_house: House = ps2.streets[i].homes[curr_estate_start_end[0]]
                    end_house: House = ps2.streets[i].homes[curr_estate_start_end[1]]
                    if not (start_house.l_fence.exists and end_house.r_fence.exists):
                        raise InvalidMove("Newly uip houses do not have fences around them")
                    # Add the length of the current estate to the set()
                    estates.update([curr_estate_start_end[1]-curr_estate_start_end[0] + 1])
                    curr_estate_start_end = [None, None]
    return estates


def get_estates_claimed_plans(gs: GameState, ps: PlayerState) -> Counter:
    """
    Returns the total number of estates that are in claimed plans.
    """
    estates: Counter = Counter()
    claimed_city_plan_indices = [i for i in range(3) if ps.city_plan_score[i] != "blank"]
    for i in claimed_city_plan_indices:
        estates.update(gs.city_plans[i].criteria)   # add the estate sizes from each claimed plan to `estates`
    return estates


def validate_move(ps1: PlayerState, ps2: PlayerState, gs: GameState) -> None:
    """
    Validates whether a move is legal or not.
    """
    built_house = {"street_ind": None,
                   "house_num": None,
                   "house_ind": None}
    ## Case: Cannot do nothing
    if ps1 == ps2: raise InvalidMove("The move can't be do nothing (must increment refusals).")
    # Counter variables
    house_counter = 0
    effect_counter = 0
    effect_played = None
    # Case: Newly built houses in ps2 cannot be already built in ps1
    for i in range(3):  # Iterate through the streets of both player states
        curr_street_1: Street = ps1.streets[i]
        curr_street_2: Street = ps2.streets[i]
        for j in range(len(curr_street_1.homes)):  # Iterate through the corresponding houses of the curr street number
            curr_house_1: House = curr_street_1.homes[j]
            curr_house_2: House = curr_street_2.homes[j]

            if curr_house_1 != curr_house_2:
                ###############
                ## Catch: built -> blank
                ##        built -> different built
                ##        built (bis) -> not bis but same number
                ##        make sure only one house is being built unless it's a bis (ensure only one bis)
                ###############
                ##### Catch errors
                ## Case: built -> blank => Error
                if curr_house_1.is_built and not (curr_house_2.is_built): raise InvalidMove(
                    "A built house cannot go to a blank house")
                ## Case: built -> (different) built => Error
                if curr_house_1.is_built and (curr_house_1.num != curr_house_2.num): raise InvalidMove(
                    "A built house cannot change nums")
                ## Case: bis'd house -> non bis'd house => Error
                if curr_house_1.is_bis and not (curr_house_2.is_bis): raise InvalidMove(
                    "A bis'd house cannot become a non bis'd house")
                ## Case-- valid: not built to built
                #   Store newly built house num into house_num
                if (not curr_house_1.is_built) and (curr_house_2.is_built and (not curr_house_2.is_bis)):
                    built_house["house_num"] = curr_house_2.num
                    built_house["street_ind"] = i
                    built_house["house_ind"] = j
                    house_counter += 1
                ##### Increment effect counter
                # If we're building a bis...
                if curr_house_2.is_bis:
                    effect_played = "bis"
                    effect_counter += 1
                ###############
                ##  Fences
                ###############
                ## Case: true fence -> false fence
                if curr_house_1.r_fence.exists and not curr_house_2.r_fence.exists: raise InvalidMove(
                    "A built fence cannot become an unbuilt fence")
                ## If we're building fences...
                if curr_house_2.r_fence.exists and not curr_house_1.r_fence.exists:
                    effect_counter += 1
                    effect_played = "surveyor"
                ###############
                ##  Used in plan
                ###############
                if curr_house_1.used_in_plan and curr_house_2.used_in_plan:
                    ## CASE 2 ##
                    if (not curr_house_1.r_fence.exists) and curr_house_2.r_fence.exists:
                        # if the house after is used in plan...
                        if curr_street_2.homes[j + 1].used_in_plan:
                            raise InvalidMove("Cannot play a fence that cuts an estate")
                if curr_house_1.used_in_plan and not curr_house_2.used_in_plan:
                    raise InvalidMove("A house that is used in plan cannot become unused in a plan")
        ###############
        ##  Parks
        ###############
        if curr_street_1.parks != curr_street_2.parks:
            ## Case: error if not ps1.parks == ps2.parks - 1
            if not (curr_street_1.parks == curr_street_2.parks - 1): raise InvalidMove(
                "The difference between PlayerState parks cannot be more than 1")
            ## If we're building parks...
            if curr_street_2.parks > curr_street_1.parks:
                if built_house["street_ind"] != i: raise InvalidMove(
                    "Parks must be played on the same street a House is built")
                effect_counter += 1
                effect_played = "landscaper"
        ###############
        ##  Pools
        ###############
        for k in range(3):
            if curr_street_2.pools[k] != curr_street_1.pools[k]:
                # Case: if going from pool -> not pool:
                if curr_street_1.pools[k] and not curr_street_2.pools[k]: raise InvalidMove("Can't deconstruct a pool")
                # Case: (valid) if going from not pool -> pool:
                if not curr_street_1.pools[k] and curr_street_2.pools[k]:
                    effect_counter += 1
                    effect_played = "pool"
    ###############
    ##  Agents
    ###############
    for i in range(6):
        curr_agents_1 = ps1.agents[i]
        curr_agents_2 = ps2.agents[i]
        if ps1.agents[i] != ps2.agents[i]:
            if curr_agents_1 + 1 != curr_agents_2: raise InvalidMove(
                "If an agent changed, the change can only be exactly += 1.")
            effect_counter += 1
    # loop through diff.non-bis-houses
    # if ps1[i] is not "blank" (aka. if ps1[i].built is not true) raise InvalidMove
    # check: make sure none of the existing house nums change/pools get removed/parks get removed/etc.
    # if diff.help_total_non_bis_houses() == 1: raise InvalidMove("Can't build more than one house
    ######
    ## Temp check
    ######
    # Construct list of house numbers from construction cards tied to "temp" effects in the game state
    house_nums_with_temp = [gs.construction_cards[i][0] for i in range(len(gs.effects)) if gs.effects[i] == "temp"]
    # Check if temps are in construction cards and is an effect played with a built house
    ## [temp has to be an effect] and [number has to be within +- 2 of one construction card]
    if ps1.temps != ps2.temps:
        if ps2.temps != ps1.temps + 1:
            raise InvalidMove("If temps is played, it can only be +1")
        if effect_played is not None:
            effect_counter += 1     # Could also have raised error here, but for debugging we thought it would
                                    # be better if we +=1 effect_counter to show 2 effects were played
        else:
            effect_counter += 1
            effect_played = "temp"
            if house_counter > 0 \
                    and ((house_nums_with_temp.count(built_house["house_num"])
                        + house_nums_with_temp.count(built_house["house_num"] + 1)
                        + house_nums_with_temp.count(built_house["house_num"] - 1)
                        + house_nums_with_temp.count(built_house["house_num"] + 2)
                        + house_nums_with_temp.count(built_house["house_num"] - 2)) == 0):
                if not ([e for e in gs.effects].count("temp") == 0): raise InvalidMove("Attempted to play a Temp when there was no construction card")
    ######
    ## Check to make sure that house_num is in the construction cards
    # Note: only need to do this check outside a "temp is played case"
    ######
    elif ([x[0] for x in gs.construction_cards].count(built_house["house_num"]) == 0) and (
                not (built_house["house_num"] is None)): raise InvalidMove("played house is not in construction cards")
    # Make sure only one effect is being played
    if effect_counter > 1: raise InvalidMove("Cannot play more than one effect in a turn")
    if effect_counter == 1 and house_counter == 0: raise InvalidMove("Cannot play effect without building a house")
    if house_counter > 1: raise InvalidMove("Cannot build more than one non-bis'd house")
    if gs.effects.count(effect_played) == 0 and (not (effect_played is None)): raise InvalidMove(
        "effect that was played is not in the Game state")
    ######
    ## Validating that played move is a valid combo in gs.construction_cards and gs.effects
    ######
    # Find the indices of the construction cards that correspond to building the built_house.num
    construction_card_indices = [i for i in range(3) if gs.construction_cards[i][0] == built_house["house_num"]]
    # If the effect is not None, check it against the gs.effects[indices] using the indices we j saved
    if effect_played is not None:
        if list(map(lambda ind: gs.effects[ind], construction_card_indices)).count(effect_played) == 0:
            raise InvalidMove("Effect played is not legal for the given house played")

    #####
    ## Check validity of pool construction
    #####
    valid_pools = [[2, 6, 7],
                   [0, 3, 7],
                   [1, 6, 10]]
    match = False
    if effect_played == "pool":
        for street in range(len(valid_pools)):  # Iterates through 0, 1, 2
            if match: break  # reduce redundant work
            for house in (valid_pools[street]):  # Iterates through [2, 6, 7], [0, 3, 7], ...
                if match: break  # reduce redundant work
                if street == built_house["street_ind"] and house == built_house["house_ind"]: match = True
        if not match:
            raise InvalidMove("Pool cannot be played on a house without a pool.")
    #####
    ## Check validity of city plans
    #####
    # Loop through ps.city_plan_score...
    for i in range(3):
        # Identify any differences
        # a. num -> "blank" (invalid)
        if ps1.city_plan_score[i] != "blank" and ps2.city_plan_score[i] == "blank":
            raise InvalidMove("Cannot go from claimed city plan score to \"blank\" city plan score.")
        # b. "blank" -> num (valid) aka. a city plan was claimed this turn
        if ps1.city_plan_score[i] == "blank" and ps2.city_plan_score[i] != "blank":
            num = ps2.city_plan_score[i]
            # i. check to make sure the correct city plan score was claimed
            # if gs.city_plans_won[i] is true AND num is ~not~ gs.city_plans[i].score2... then error.
            if gs.city_plans_won[i] and num != gs.city_plans[i].score2:
                raise InvalidMove("If a city plan was claimed by a player, BUT they weren't the first to claim that "
                                  "plan, the score claimed CANNOT be anything BUT the corresponding plan's score 2.")
            # if gs.city_plans_won[i] is false AND num is ~not~ gs.city_plans[i].score1 then error.
            if not gs.city_plans_won[i] and num != gs.city_plans[i].score1:
                raise InvalidMove("If a city plan was claimed, AND they were the first to claim that plan, "
                                  "the score claimed CANNOT be anything BUT the corresponding plan's score 1.")
    # validate that the total number uip houses match with the number of total estates that
    # are in all won city plans.
    ps_uip_estates: Counter = get_estates(ps1, ps2)
    claimed_plans_estates: Counter = get_estates_claimed_plans(gs, ps2)
    # Only check if uip_estates matches claimed_plan_estates if we're claiming estates that turn
    #   This is to account for two cases:
    #       1. Invalid ps1 uip and claimed_estates, but newly claimed uip houses matches newly claimed plan
    #       2. No change between ps1 and ps2 uip houses or claimed_plans
    #       since we only count houses that change between ps1 and ps2, case 2 errored because it said ps_uip_estates
    #       was empty.
    if ps1.city_plan_score != ps2.city_plan_score and ps_uip_estates != claimed_plans_estates:
        raise InvalidMove("Cannot claim a plan when used-in-plan houses don't satisfy the plan.")

    #######
    ## Refusals checking
    #######
    # Basically check if refusals changed iff there is no move that can be played
    if GenValidMove(gs, ps1).vm.refusals != ps2.refusals: raise InvalidMove(
        "Cannot increment refusals if a valid move exists.")
    if (ps2.refusals != ps1.refusals) and (effect_counter != 0 or house_counter != 0):
        raise InvalidMove("Cannot increment refusals and play a house/effect")
