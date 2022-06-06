import sys
sys.path.append('../../')
from my_python.PlayerState import PlayerState
from my_python.GameState import GameState
from my_python.Street import Street
from my_python.House import House
from my_python.exceptions import InvalidMove

def validate_move(diff: PlayerState, ps1: PlayerState, ps2: PlayerState, gs: GameState) -> None:
    ## Case: Cannot do nothing
    if ps1 == ps2: raise InvalidMove("The move can't be do nothing (must increment refusals).")
    # Counter variables
    house_counter = 0
    effect_counter = 0
    house_num = None
    # Case: Newly built houses in ps2 cannot be already built in ps1
    for i in range(3):  # Iterate through the streets of both player states
        curr_street_1: Street = ps1.streets[i]
        curr_street_2: Street = ps2.streets[i]
        for j in range(len(curr_street_1.homes)):
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
                if curr_house_1.is_built and not (curr_house_2.is_built): raise InvalidMove("A built house cannot go to a blank house")
                ## Case: built -> (different) built => Error
                if curr_house_1.is_built and (curr_house_1.num != curr_house_2.num): raise InvalidMove("A built house cannot change nums")
                ## Case: bis'd house -> non bis'd house => Error
                if curr_house_1.is_bis and not (curr_house_2.is_bis): raise InvalidMove("A bis'd house cannot become a non bis'd house")
                ## Case-- valid: not built to built
                #   Store newly built house num into house_num
                if (not curr_house_1.is_built) and curr_house_2.is_built: house_num = curr_house_2.num
                ##### Increment effect counter
                # If we're building a bis...
                if curr_house_2.is_bis: effect_counter += 1
                # If we're building a non-bis house...
                if curr_house_2.is_built and not curr_house_1.is_built: house_counter += 1
                ###############
                ## Fences: true fence becomes false fence
                ###############
                ## Case: true fence -> false fence
                if curr_house_1.r_fence.exists and not curr_house_2.r_fence.exists: raise InvalidMove("A built fence cannot become an unbuilt fence")
                ## If we're building fences...
                if curr_house_2.r_fence.exists: effect_counter += 1
    # loop through diff.non-bis-houses
    # if ps1[i] is not "blank" (aka. if ps1[i].built is not true) raise InvalidMove
    # check: make sure none of the existing house nums change/pools get removed/parks get removed/etc.
    if diff.help_total_non_bis_houses() == 1: raise InvalidMove("Can't build more than one house.")
    if not ((ps2.get_num_played_effects() - ps1.get_num_played_effects()) in {0, 1}): raise InvalidMove("Can't remove effects or play more than one effect.")
    ## Check: make sure the only valid combos for newly built houses are (1) 1 house + 1 bis and
    #                                                                    (2) 1 house
    # if house_counter == 0: raise
    # Check: make sure that multiple fences are not being built on the same turn
    if effect_counter > 1: raise InvalidMove("Cannot play more than one effect in a turn")
    if house_counter > 1: raise InvalidMove("Cannot build more than one new house")
    if effect_counter == 1 and house_counter == 0: raise InvalidMove("Cannot play effect without building a house")
    # check to make sure that house_num is in the construction cards
    if ([x[0] for x in gs.construction_cards].count(house_num) == 0) and not (house_num is None): raise InvalidMove("played house is not in construction cards")




