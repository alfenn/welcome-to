import copy
import sys
from typing import Tuple, List

from my_python.House import House
from my_python.Street import Street
from my_python.PlayerState import PlayerState
from my_python.GameState import GameState

sys.path.append('../../../../')


def get_exclusive_range(s: Street, i: int) -> Tuple:
    """
        Generates the range of valid house numbers (exclusive) from
        given Street and house index inputs.
            a.k.a. Returns a tuple of the left and right adjacent built houses from a given
            house index `i`.
            Used for finding out if [x] [ ] [ ] [ ] [x] actually allows us to build a new house.

        :param s: Homes we are looking at (Homes on a Street)
        :param i: the house index representing the current house we are on in the Homes
        :return: Tuple of length 2
    """
    i_is_first = i == 0
    i_is_last = i == len(s.homes) - 1
    min_house_num = -1
    max_house_num = 18
    j = i - 1
    # Iterate to the front (min = largest value on left) -> find "largest min"
    while j >= 0 and not i_is_first:
        curr_house: House = s.homes[j]
        if curr_house.is_built:
            if curr_house.num > min_house_num: min_house_num = curr_house.num
        j -= 1
    j = i + 1
    # Iterate to the back (max = smallest value on the right) -> find "smallest max"
    while j <= len(s.homes) - 1 and not i_is_last:
        curr_house: House = s.homes[j]
        if curr_house.is_built:
            if curr_house.num < max_house_num: max_house_num = curr_house.num
        j += 1
    return min_house_num, max_house_num


def vm_construction_card_index(cc: List[List], exclusive_range: Tuple[int]) -> int:
    """
    Returns index of the construction card ( [0,2] ) that can be played as a valid move
    with a given exclusive range.
    :param cc: list of construction cards [num, effect]
    :param exclusive_range: exclusive range for valid construction cards
    :return: index of construction card ([0, 2]) that is a valid move. returns -1 if
             no construction cards can be played.
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
    house_were_building: House = ps.streets[st_i].homes[h_i]
    house_were_building.num = cc[0]
    house_were_building.is_built = True
    return ps


class MoveGeneratorInterface:
    def __init__(self):
        # Initialize instance variables
        self.vm: PlayerState = None
        self.ps: PlayerState = None
        self.gs: GameState = None

    def generate(self, gs: GameState, ps: PlayerState) -> PlayerState:
        """Algorithm for generating a valid move"""
        pass


class MoveGenerator1(MoveGeneratorInterface):
    def generate(self, gs: GameState, ps: PlayerState) -> PlayerState:
        self.vm = copy.deepcopy(ps)
        self.ps = ps
        self.gs = gs
        house_built = False
        # Loop through all the streets
        for i in range(3):
            if house_built: break
            # Loop through all the homes in the street
            for j in range(len(self.ps.streets[i].homes)):
                curr_house: House = self.ps.streets[i].homes[j]
                # If the house is not built...
                if not curr_house.is_built and not curr_house.is_roundabout:
                    excl_range = get_exclusive_range(self.ps.streets[i], j)
                    # If the difference between the returned "max" and "min" is equal to 1,
                    #   skip to the next street
                    if excl_range[1] - excl_range[0] == 1: continue
                    # Elif a valid range exists...
                    #   See if a construction card in the `gs` can indeed be played in this range.
                    vm_card_ind = vm_construction_card_index(self.gs.construction_cards, excl_range)
                    if vm_card_ind == -1: continue
                    # Else a valid cc exists for this blank spot...
                    #   update the `vm` PlayerState to play the construction card
                    self.vm = update_ps_w_valid_card(cc=self.gs.construction_cards[vm_card_ind],
                                                     ps=self.vm,
                                                     st_i=i,
                                                     h_i=j)
                    house_built = True
                    break
        if not house_built:
            # Increment refusals
            self.vm.refusals += 1
        ### Now self.vm is a PlayerState with the valid move (if there is one) played
        return self.vm
