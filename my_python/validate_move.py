import copy
import json
import sys
from collections import Counter  # https://docs.python.org/3/library/collections.html#collections.Counter
from typing import Tuple

sys.path.append('../../')
from my_python.PlayerState import PlayerState
from my_python.GameState import GameState
from my_python.Street import Street, PARK_MAX
from my_python.House import House
from my_python.exceptions import InvalidMove
from my_python.MoveGeneratorInterface import MoveGenerator1
from my_python.contracts import ACCEPTABLE_CRITERIA_CARD_1S, ACCEPTABLE_CRITERIA_CARD_2S


# Put this as helper that takes ps1 and ps2 because of the assumption that ps1 is correct:
#   https://piazza.com/class/l0wlxndauhb4xv?cid=163
def get_claimed_estates(ps1: PlayerState, ps2: PlayerState) -> list:
    """
    Returns a list of: [0] = set such that it holds all the estates that are uip composed
    of only the houses that changed; [1] = bool flag set to whether there are non-estate uip houses added.
    """
    estates: Counter = Counter()
    non_estate_uip_houses = False
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
                        curr_estate_start_end[1] = j  # set end house to j
                    if (not curr_house.used_in_plan) or (not curr_house.is_built):
                        counting_houses = False
                        curr_estate_start_end[1] = j - 1  # set end house to j-1 bc current house isn't part of estate
                # Check if we should be adding the current estate, or if we should error
                if (not counting_houses) and (curr_estate_start_end != [None, None]):  # not counting and we have
                    # an estate saved.
                    # If the estate doesn't have a left and right fence then error
                    start_house: House = ps2.streets[i].homes[curr_estate_start_end[0]]
                    end_house: House = ps2.streets[i].homes[curr_estate_start_end[1]]
                    if not (start_house.l_fence.exists and end_house.r_fence.exists):
                        # Note: setting the flag instead of erroring when we encounter non-estate-newly-uip-houses bc
                        #   in adv-cri where we claim [all-houses-in-row], we don't want to error.
                        #   But in case where no adv-plans were claimed, we want to know this so we can throw the
                        #   error that there were houses that were erroneously marked uip.
                        # raise InvalidMove("Newly uip houses do not have fences around them")
                        non_estate_uip_houses = True
                    # Add the length of the current estate to the set()
                    estates.update([curr_estate_start_end[1] - curr_estate_start_end[0] + 1])
                    curr_estate_start_end = [None, None]
    return [estates, non_estate_uip_houses]


def get_claimed_plans(gs: GameState, ps1: PlayerState, ps2: PlayerState) -> list:
    """
    Returns a list with ind 0 = the total number of non_advanced_criteria_estates that are in claimed plans, and
    ind 1 = list of advanced city plans.
    """
    advanced_city_plan_criteria: list = ACCEPTABLE_CRITERIA_CARD_1S + ACCEPTABLE_CRITERIA_CARD_2S
    non_advanced_criteria_estates: Counter = Counter()
    advanced_city_plans_claimed = []
    # Grab indices for plans that were claimed this turn
    claimed_city_plan_indices = [i for i in range(3) if ps2.city_plan_score[i] != ps1.city_plan_score[i]]
    for i in claimed_city_plan_indices:
        curr_city_plan_criteria = gs.city_plans[i].criteria
        # If curr_city_plan_criteria isn't an advanced_city_plan, update `non_advanced_criteria_estates`
        if curr_city_plan_criteria not in advanced_city_plan_criteria:
            non_advanced_criteria_estates.update(
                curr_city_plan_criteria)  # add the estate sizes from each claimed plan to `non_advanced_criteria_estates`
        # If curr_city_plan_criteria is an advanced_city_plan,
        else:
            advanced_city_plans_claimed.append(curr_city_plan_criteria)
    return [non_advanced_criteria_estates, advanced_city_plans_claimed]

def check_advanced_plans(advanced_criteria, ps1: PlayerState, ps2: PlayerState) -> None:
    """Errors if advanced plan criteria is not satisfied."""
    def _curr_street_has_all_parks(i: int) -> bool:
        return ps2.streets[i].parks == PARK_MAX[i]

    def _curr_street_has_all_pools(i: int) -> bool:
        return ps2.streets[i].pools == [True, True, True]

    ## Case: ["all houses", ~0|2]
    if type(advanced_criteria) == list and advanced_criteria[0] == "all houses":
        street_ind = advanced_criteria[1]
        curr_street_1 = ps1.streets[street_ind]
        curr_street_2 = ps2.streets[street_ind]
        # Check every house in the street
        for house_ind in range(len(curr_street_2.homes)):
            curr_house_1 = curr_street_1.homes[house_ind]
            curr_house_2 = curr_street_2.homes[house_ind]
            # Check: house was not built
            if not curr_house_2.is_built:
                raise InvalidMove(f"Attempted to claim [\"all houses\", {street_ind}] but house at ind {house_ind} was not built")
            # Check: house must be newly claimed
            if not (curr_house_2.used_in_plan and not curr_house_1.used_in_plan):
                raise InvalidMove(f"Attempted to claim advanced plan but house at ind ({street_ind}, {house_ind}) wasn't newly claimed")
    ## Case: "end houses"
    elif advanced_criteria == "end houses":
        for street_ind in range(3):
            curr_street_1 = ps1.streets[street_ind]
            curr_street_2 = ps2.streets[street_ind]
            for house_ind in [0, len(curr_street_2.homes)-1]:
                curr_house_1 = curr_street_1.homes[house_ind]
                curr_house_2 = curr_street_2.homes[house_ind]
                # Check: house was not built
                if not curr_house_2.is_built:
                    raise InvalidMove(f"Attempted to claim \"end houses\" but house at ind ({street_ind}, {house_ind}) was not built")
                # Check: house must be newly claimed
                if not (curr_house_2.used_in_plan and not curr_house_1.used_in_plan):
                    raise InvalidMove(f"Attempted to claim advanced plan but house at ind ({street_ind}, {house_ind}) wasn't newly claimed")
    ## Case: "7 temps"
    elif advanced_criteria == "7 temps":
        temps_played = ps2.temps
        if temps_played < 7: raise InvalidMove(f"Attempted to claim \"7 temps\" but there are only {temps_played} temps played")
    ## Case: "5 bis"
    elif advanced_criteria == "5 bis":
        street_has_five_bis = False
        for street_ind in range(3):
            if street_has_five_bis: break
            curr_street = ps2.streets[street_ind]
            # increment bis_counter to keep track of the number of bis'd houses on the street
            bis_counter = 0
            for curr_house in curr_street.homes:
                if curr_house.is_bis: bis_counter += 1
                # if we are equal to 5 bis on the curr_street...
                if bis_counter == 5:
                    street_has_five_bis = True
                    break
        if not street_has_five_bis: raise InvalidMove(f"Attempted to claim \"5 bis\" but there is less than 5 bis played on the same street")
    ## Case: "two streets all parks"
    elif advanced_criteria == "two streets all parks":
        streets_w_all_parks = []
        for street_ind in range(3):
            if _curr_street_has_all_parks(street_ind):
                streets_w_all_parks.append(street_ind)
        if len(streets_w_all_parks) < 2:
            raise InvalidMove(f"Attempted to claim \"two streets all parks\" but only street ind {streets_w_all_parks} have all parks")
    ## Case: "two streets all pools"
    elif advanced_criteria == "two streets all pools":
        streets_w_all_pools = []
        for street_ind in range(3):
            if _curr_street_has_all_pools(street_ind):
                streets_w_all_pools.append(street_ind)
        if len(streets_w_all_pools) < 2:
            raise InvalidMove(f"Attempted to claim \"two streets all pools\" but only street ind {streets_w_all_pools} have all pools")
    ## Case: ["all pools all parks", ~1|2]
    elif type(advanced_criteria) == list and advanced_criteria[0] == "all pools all parks":
        street_ind = advanced_criteria[1]
        has_all_pools = _curr_street_has_all_pools(street_ind)
        has_all_parks = _curr_street_has_all_parks(street_ind)
        if not (has_all_pools and has_all_parks):
            raise InvalidMove(f"Attempted to claim [\"all pools all parks\", {street_ind}] but has_all_pools is {has_all_pools} and has_all_parks is {has_all_parks}")
    ## Case: "all pools all parks one roundabout"
    elif advanced_criteria == "all pools all parks one roundabout":
        street_w_all_pools_all_parks_exists = False
        for street_ind in range(3):
            curr_street: Street = ps2.streets[street_ind]
            has_all_pools = _curr_street_has_all_pools(street_ind)
            has_all_parks = _curr_street_has_all_parks(street_ind)
            has_roundabout = curr_street.get_num_roundabouts() > 0
            if has_all_pools and has_all_parks and has_roundabout:
                street_w_all_pools_all_parks_exists = True
        if street_w_all_pools_all_parks_exists is False:
            raise InvalidMove("Tried to claim \"all pools all parks one roundabout\" but there is no street meeting this condition")
    return None






######################################
## The validate_move function ########
######################################

def validate_move(ps1: PlayerState, ps2: PlayerState, gs: GameState) -> None:
    """
    Validates whether a move is legal or not.
    """
    def _identify_roundabouts() -> Tuple:
        """
        Checks for roundabouts and returns a list with [0] being appropriate flag and [1] being the roundabout location.
        Errors if more than one roundabout was played.
        """
        played: bool = False
        location: Tuple = (None, None)
        for i in range(3):
            curr_street_1: Street = ps1.streets[i]
            curr_street_2: Street = ps2.streets[i]
            for j in range(len(curr_street_1.homes)):
                curr_house_1: House = curr_street_1.homes[j]
                curr_house_2: House = curr_street_2.homes[j]
                ## If we are building a roundabout...
                if curr_house_1.is_roundabout and not curr_house_2.is_roundabout:
                    raise InvalidMove("A roundabout cannot be deleted")
                if not curr_house_1.is_roundabout and curr_house_2.is_roundabout:
                    if played:
                        raise InvalidMove("Cannot play two roundabouts in one move")
                    else:  # roundabout has not been played
                        played = True
                        location = (i, j)
        return location
    def _only_diff_is_not_uip_to_uip(h1: House, h2: House) -> bool:
        if h1.used_in_plan is False and h2.used_in_plan is True:
            h1_claim_uip = copy.deepcopy(h1)
            h1_claim_uip.used_in_plan = True
            if h1_claim_uip == h2:
                return True
        return False
    built_house = {"street_ind": None,
                   "house_num": None,
                   "house_ind": None}
    ## Case: Cannot do nothing
    if ps1 == ps2: raise InvalidMove("The move can't be do nothing (must increment refusals).")
    # Counter variables
    house_counter = 0
    effect_counter = 0
    effect_played = None
    roundabout_location = _identify_roundabouts()  # Sets roundabout location, and also makes sure at most 1 roundabout was played

    # Case: Newly built houses in ps2 cannot be already built in ps1
    for i in range(3):  # Iterate through the streets of both player states
        curr_street_1: Street = ps1.streets[i]
        curr_street_2: Street = ps2.streets[i]
        for j in range(len(curr_street_1.homes)):  # Iterate through the corresponding houses of the curr street number
            curr_house_1: House = curr_street_1.homes[j]
            curr_house_2: House = curr_street_2.homes[j]

            if not _only_diff_is_not_uip_to_uip(curr_house_1, curr_house_2):
                ###############
                ## Catch: built -> blank
                ##        built -> different built
                ##        built (bis) -> not bis but same number
                ##        make sure only one house is being built unless it's a bis (ensure only one bis)
                ###############
                ##### Catch errors
                ## Case: built -> blank => Error
                if curr_house_1.is_built and not curr_house_2.is_built: raise InvalidMove(
                    "A built house cannot go to a blank house")
                ## Case: built -> (different) built => Error
                if curr_house_1.is_built and (curr_house_1.num != curr_house_2.num): raise InvalidMove(
                    "A built house cannot change nums")
                ## Case: bis'd house -> non bis'd house => Error
                if curr_house_1.is_bis and not curr_house_2.is_bis: raise InvalidMove(
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
                if not curr_house_1.is_bis and curr_house_2.is_bis:
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
                    if (i, j + 1) == roundabout_location:
                        continue
                    elif (i, j) == roundabout_location:
                        continue
                    else:
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
            effect_played = "agent"
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
            effect_counter += 1  # Could also have raised error here, but for debugging we thought it would
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
                if not ([e for e in gs.effects].count("temp") == 0): raise InvalidMove(
                    "Attempted to play a Temp when there was no construction card")
    ######
    ## Check to make sure that house_num is in the construction cards
    # Note: only need to do this check outside a "temp is played case"
    ######
    elif ([x[0] for x in gs.construction_cards].count(built_house["house_num"]) == 0) and (
            not (built_house["house_num"] is None)):
        raise InvalidMove("played house is not in construction cards")
    # Make sure only one effect is being played
    if effect_counter > 1: raise InvalidMove("Cannot play more than one effect in a turn")
    if effect_counter == 1 and house_counter == 0: raise InvalidMove("Cannot play effect without building a house")
    if house_counter > 1: raise InvalidMove("Cannot build more than one non-bis'd house")
    if gs.effects.count(effect_played) == 0 and (not (effect_played is None)): raise InvalidMove(
        "effect that was played is not in the Game state")
    ##############
    ## Validating that played move is a valid combo in gs.construction_cards and gs.effects
    ##############
    # Find the indices of the construction cards that correspond to building the built_house.num
    construction_card_indices = [i for i in range(3) if gs.construction_cards[i][0] == built_house["house_num"]]
    if effect_played == "temp":
        construction_card_indices += [i for i in range(3) if
                                      (gs.construction_cards[i][0] == built_house["house_num"] + 1
                                       or gs.construction_cards[i][0] == built_house["house_num"] - 1
                                       or gs.construction_cards[i][0] == built_house["house_num"] + 2
                                       or gs.construction_cards[i][0] == built_house["house_num"] - 2)]
    # If the effect is not None, check it against the gs.effects[indices] using the indices we j saved
    elif effect_played is not None:
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
    ps_uip_estates: list = get_claimed_estates(ps1, ps2)
    claimed_plans: list = get_claimed_plans(gs, ps1, ps2)
    # Only check if uip_estates matches claimed_plans__non_adv_cri_estates if we're claiming estates that turn
    #   This is to account for two cases:
    #       1. Invalid ps1 uip and claimed_estates, but newly claimed uip houses matches newly claimed plan
    #       2. No change between ps1 and ps2 uip houses or claimed_plans
    #       since we only count houses that change between ps1 and ps2, case 2 errored because it said ps_uip_estates
    #       was empty.
    ## Check: non-advanced case:
    if claimed_plans[1] == []:
        if ps_uip_estates[0] != claimed_plans[0]:
            raise InvalidMove("Cannot claim a plan when used-in-plan houses don't satisfy the plan.")
        if ps_uip_estates[1] is True:
            raise InvalidMove("Newly uip houses are not estates, and no adv-plans were claimed. (aka. we found that newly uip houses do not have fences around the first and last uip house in that block of uip-houses)")
    ## Check: advanced case
    else:
        ## Subcheck 1: claimed_plans_non-advanced-criteria-estates must be satisfied
        if not (claimed_plans[0] - ps_uip_estates[0] == Counter()):
            raise InvalidMove("Cannot claim a plan when used-in-plan houses don't satisfy the plan.")
        ## Subcheck 2: make sure playerstate satisfies claimed_plans_advanced-criteria
        for ac in claimed_plans[1]:
            check_advanced_plans(ac, ps1, ps2)

    #######
    ## Refusals checking
    #######
    # Basically check if refusals changed iff there is no move that can be played
    move_generator = MoveGenerator1()
    generated_move_ps = move_generator.generate(gs, ps1)
    ## Check: [2nd cond] don't error if the reason for the refusal difference is bc the only valid move available
    #   (a roundabout move) was played
    if generated_move_ps.refusals != ps2.refusals \
            and (ps1.get_total_num_roundabouts() == ps2.get_total_num_roundabouts()):
        raise InvalidMove("Cannot increment refusals if a valid move exists.")
    if house_counter == 0 and ps1.refusals == ps2.refusals:
        raise InvalidMove("Cannot keep refusals the same if no house was built.")
    if (ps2.refusals != ps1.refusals) and (effect_counter != 0 or house_counter != 0):
        raise InvalidMove("Cannot increment refusals and play a house/effect")
