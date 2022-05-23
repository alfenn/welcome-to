import sys
sys.path.append('../../')
from my_python.PlayerState import PlayerState
from my_python.exceptions import InvalidMove

def validate_move(diff: PlayerState) -> None:
    if diff.help_total_non_bis_houses() > 1: raise InvalidMove("Can't build more than one house.")



