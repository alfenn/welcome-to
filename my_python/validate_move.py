import sys
sys.path.append('../../')
from my_python.PlayerState import PlayerState
from my_python.Street import Street
from my_python.House import House
from my_python.exceptions import InvalidMove

def validate_move(diff: PlayerState, ps1: PlayerState, ps2: PlayerState) -> None:
    ## Case: Cannot do nothing
    if ps1 == ps2: raise InvalidMove("The move can't be do nothing (must increment refusals).")
    # Case: Newly built houses in ps2 cannot be already built in ps1
    for i in range(3):  # Iterate through the streets of both player states
        curr_street_1: Street = ps1.streets[i]
        curr_street_2 = ps2.streets[i]
        # curr_street_diff = diff.streets[i]
        for j in range(len(curr_street_1.homes)):
            curr_house_1: House = curr_street_1.homes[j]
            curr_house_2: House = curr_street_2.homes[j]
            # curr_house_diff: House = curr_street_diff.homes[j]
            ## Catch: built -> blank
            ##        built -> different built
            ##        blank -> built
            if curr_house_1.num != curr_house_2.num:
                ## Case: built -> blank => Error
                if curr_house_1.is_built and not (curr_house_2.is_built): raise InvalidMove("A built house cannot go to a blank house")
                ## Case: built -> (different) built => Error
                if curr_house_1.is_built and curr_house_2.is_built: raise InvalidMove("A built house cannot change nums")
                ## Case: bis'd house -> non bis'd house => Error
                if curr_house_1.is_bis and not (curr_house_2.is_bis): raise InvalidMove("A bis'd house cannot become a non bis'd house")
    # loop through diff.non-bis-houses
    # if ps1[i] is not "blank" (aka. if ps1[i].built is not true) raise InvalidMove
    # check: make sure none of the existing house nums change/pools get removed/parks get removed/etc.
    if diff.help_total_non_bis_houses() == 1: raise InvalidMove("Can't build more than one house.")
    if not ((ps2.get_num_played_effects() - ps1.get_num_played_effects()) in {0, 1}): raise InvalidMove("Can't remove effects or play more than one effect.")



