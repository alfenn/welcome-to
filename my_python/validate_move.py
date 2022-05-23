import sys
sys.path.append('../../')
from my_python.PlayerState import PlayerState
from my_python.exceptions import InvalidMove

def validate_move(diff: PlayerState, ps1: PlayerState, ps2: PlayerState) -> None:
    if ps1 == ps2: raise InvalidMove("The move can't be do nothing (must increment refusals).")
    # loop through diff.non-bis-houses
    # if ps1[i] is not "blank" (aka. if ps1[i].built is not true) raise InvalidMove
    # check: make sure none of the existing house nums change/pools get removed/parks get removed/etc.
    if diff.help_total_non_bis_houses() == 1: raise InvalidMove("Can't build more than one house.")
    if not ((ps2.get_num_played_effects() - ps1.get_num_played_effects()) in {0, 1}): raise InvalidMove("Can't remove effects or play more than one effect.")



