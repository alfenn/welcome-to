import sys
sys.path.append('../../')
from my_python.archive.a3.PlayerState import PlayerState
from my_python.OldGameState import OldGameState

def gen_move(ps1: PlayerState, ps2: PlayerState) -> PlayerState:
    """Generates a player state corresponding to the exact move made
    from the two PlayerState arguments.

    :return: PlayerState with "same" for values that are the same
    across ps1 and ps2, and the value for ps2 when they differ.
    """

class IsValidMove:
    def __init__(self, gs: OldGameState, ps1: PlayerState, ps2: PlayerState):
        self.gs: OldGameState = gs
        self.ps1: PlayerState = ps1
        self.ps2: PlayerState = ps2
        self.ps_move: PlayerState = gen_move(ps1, ps2)

    def calc_is_valid_move(self) -> bool:
        """Worker function that determines if the move specified by the class
        arguments is valid."""
        ####### Do some work on self.ps_move

    def __str__(self):
        """Returns json boolean corresponding to whether the move specified
        by the class arguments is valid."""
        if self.calc_is_valid_move(): return "true"
        return "false"
