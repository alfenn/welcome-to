import sys
from typing import Tuple

from archive.OldGameState import OldGameState

sys.path.append('../../../../')
from my_python.archive.a3.PlayerState import *
from my_python.archive.a3.House import House


def get_exclusive_range(h: Homes, i: int) -> Tuple:
    """
        Generates the range of valid house numbers (exclusive) from
        given Street and house index inputs.

        :param h: Homes we are looking at (Homes on a Street)
        :param i: the house index representing the current house we are on in the Homes
        :return: Tuple of length 2
    """
    i_is_first = i==0
    i_is_last = i==h.get_num_houses()-1
    min_house_num = -1
    max_house_num = 18
    j = i-1
    # Iterate to the front (min = largest value on left) -> find "largest min"
    while j >= 0 and not i_is_first:
        curr_home = h.get(j)
        if curr_home.house.is_built():
            if curr_home.house.num > min_house_num: min_house_num = curr_home.house.num
        j -= 1
    j = i+1
    # Iterate to the back (max = smallest value on the right) -> find "smallest max"
    while j <= h.get_num_houses() - 1 and not i_is_last:
        curr_home = h.get(j)
        if curr_home.house.is_built():
            if curr_home.house.num < max_house_num: max_house_num = curr_home.house.num
        j += 1
    return min_house_num, max_house_num

def vm_construction_card_index(cc: List[List], exclusive_range: Tuple[int]) -> int:
    """
        Figures out which construction card can be played as a valid move with
        a given exclusive range.

        :param cc: list of construction cards [num, effect]
        :param exclusive_range: exclusive range for valid construction cards
        :return: index of the construction card that is a valid move;
            -1 if no construction cards can be played
    """
    valid_index = -1
    for i, card in enumerate(cc):
        if exclusive_range[0] < cc[i][0] < exclusive_range[1]:
            valid_index = i
            return valid_index
    return valid_index

def update_ps_w_valid_card(cc: list, ps: PlayerState, st_i: int, h_i: int) -> PlayerState:
    """
        Updates a given PlayerState by building a house using the given card
        at the given index.

        :param cc: the construction card that we want to build a House with
        :param ps: the PlayerState we are building a house within
        :param st_i: the index for the street we're building the house on
        :param h_i: the index for the house we're building the house on
    """
    ps.streets[st_i].homes.get(h_i).house.num = cc[0]
    return ps


class GenValidMove:
    def __init__(self, gs: OldGameState, ps: PlayerState):
        """
            Initialize a class with methods to help us generate a valid move,
            returning a PlayerState with the valid move played, or refusals
            incremented when printed.

            :param gs: the OldGameState representation
            :param ps: the PlayerState representation
        """
        ################### Initialize valid move field
        self.vm: PlayerState = ps
        ################### Algorithm for generating a valid move
        card_played = False
        # Loop through all the streets
        for i in range(3):
            if card_played: break
            # Loop through all the homes in the street
            for j in range(ps.streets[i].homes.get_num_houses()):
                curr_house: House = ps.streets[i].homes.get(j).house
                # If the house is built...
                if not curr_house.is_built():
                    excl_range = get_exclusive_range(ps.streets[i].homes, j)
                    # If the difference between the returned "max" and "min" is equal to 1,
                    #   skip to the next street
                    if excl_range[1] - excl_range[0] == 1: continue
                    # Elif a valid range exists...
                    vm_card_ind = vm_construction_card_index(gs.construction_cards, excl_range)
                    if vm_card_ind == -1: continue
                    # Else a valid cc exists for this blank spot...
                    #   update the `vm` PlayerState to play the construction card
                    self.vm = update_ps_w_valid_card(cc=gs.construction_cards[vm_card_ind],
                                           ps=self.vm,
                                           st_i=i,
                                           h_i=j)
                    card_played = True
                    break
        if not card_played:
            # Increment refusals
            self.vm.refusals += 1
        ######### Now self.vm is a PlayerState with the valid move (if there is) played.

    def __str__(self) -> str:
        """
            Returns the played move as a json string representation of
            the resulting PlayerState.

            :return: json string of a PlayerState
        """
        return str(self.vm)

