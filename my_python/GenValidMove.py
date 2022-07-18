import copy
import sys
from typing import Tuple, List

from my_python.House import House
from my_python.Street import Street
from my_python.PlayerState import PlayerState
from my_python.OldGameState import OldGameState

sys.path.append('../../../../')


def get_exclusive_range(s: Street, i: int) -> list:
    """
        Generates the range of valid house numbers (exclusive) from
        given Street and house index inputs in the form of Tuple of len 2 for
        normal range, and roundabout range.
            a.k.a. Returns a tuple of the left and right adjacent built houses from a given
            house index `i`.
            Used for finding out if [x] [ ] [ ] [ ] [x] actually allows us to build a new house.

        :param s: Homes we are looking at (Homes on a Street)
        :param i: the house index representing the current house we are on in the Homes
        :return: List
            [Tuple of len 2--normal range,
            bool--if roundabout can be played in this gap, aka if gap_size >= 2,
            Tuple of len 2--roundabout range]
    """
    i_is_first = i == 0
    i_is_last = i == len(s.homes) - 1
    min_house_num = 0
    max_house_num = 16
    size_of_gap = 0
    # Start at i and iterate left until you hit a built house or the left-side
    j = i
    # Iterate to the front (min = largest value on left) -> find "largest min"
    while j >= 0 and not i_is_first:
        curr_house: House = s.homes[j]
        size_of_gap += 1
        if curr_house.is_built:
            if curr_house.num > min_house_num: min_house_num = curr_house.num
            break
        j -= 1
    # Then start at i+1 and iterate right until you hit a built house or the right-side
    j = i + 1
    # Iterate to the back (max = smallest value on the right) -> find "smallest max"
    while j <= len(s.homes) - 1 and not i_is_last:
        curr_house: House = s.homes[j]
        size_of_gap += 1
        if curr_house.is_built:
            if curr_house.num < max_house_num: max_house_num = curr_house.num
            break
        j += 1
    return [(min_house_num, max_house_num), size_of_gap >= 2, (0, max_house_num)]


def update_ps_w_valid_card(cc_or_roundabout, ps: PlayerState, st_i: int, h_i: int) -> PlayerState:
    """
    Updates a given PlayerState by building a house using the given card
    at the given index.

    :param cc: construction card to be built | "roundabout"
    :param ps: the PlayerState we are building a house within
    :param st_i: the index for the street we're building the house on
    :param h_i: the index for the house we're building the house on
    """
    house_were_building: House = ps.streets[st_i].homes[h_i]
    if type(cc_or_roundabout) == list:
        house_were_building.num = cc_or_roundabout[0]
        house_were_building.is_built = True
    elif cc_or_roundabout == "roundabout":
        house_were_building.is_roundabout = True
    return ps


class GenValidMove:
    def __init__(self):
        # Initialize valid move field
        self.vm: PlayerState = None
        self.ps: PlayerState = None
        self.gs: OldGameState = None

    def __str__(self) -> str:
        """
        Returns the played move as a json string representation of
        the resulting PlayerState.

        :return: json string of a PlayerState
        """
        return str(self.vm)

    def _vm_construction_card_index(self, exclusive_range: Tuple[int]) -> int:
        """
        Returns gs.construction_card index of the construction card that can be played as a valid move
        with a given exclusive range.
        :param exclusive_range: exclusive range for valid construction cards
        :return: index of construction card that is a valid move. returns -1 if
                 no construction cards can be played.
        """
        cc: List[list] = self.gs.construction_cards     # cc: list of construction cards [num, effect]
        valid_index = -1
        for i, card in enumerate(cc):
            if exclusive_range[0] < cc[i][0] < exclusive_range[1]:
                valid_index = i
                return valid_index
        return valid_index

    def _play_construction_card_if_allowed(self, i_street_index: int, i_house_index: int, i_play_roundabout: bool, i_excl_range_t: Tuple) -> bool:
        """Play construction card if allowed, and return bool specifying whether a house was built or not."""
        # See if a construction card in the `gs` can indeed be played in this range.
        vm_card_ind = self._vm_construction_card_index(i_excl_range_t)
        if vm_card_ind != -1:
            # A valid cc exists for this blank spot...
            if not i_play_roundabout:
                # Play the cc at st_i=i_street_index, h_i=i_house_index
                self.vm = update_ps_w_valid_card(cc_or_roundabout=self.gs.construction_cards[vm_card_ind],
                                                 ps=self.vm,
                                                 st_i=i_street_index,
                                                 h_i=i_house_index)
            else:
                # Play a roundabout at st_i=i_street_index, h_i=i_house_index and
                #   play the cc at st_i=i_street_index, h_i=i_house_index + 1
                self.vm = update_ps_w_valid_card(cc_or_roundabout="roundabout",
                                                 ps=self.vm,
                                                 st_i=i_street_index,
                                                 h_i=i_house_index)
                self.vm = update_ps_w_valid_card(cc_or_roundabout=self.gs.construction_cards[vm_card_ind],
                                                 ps=self.vm,
                                                 st_i=i_street_index,
                                                 h_i=i_house_index + 1)
            return True
        return False

    def generate(self, gs: OldGameState, ps: PlayerState) -> PlayerState:
        """
        Algorithm for generating a valid move
        """
        self.vm = copy.deepcopy(ps)
        self.ps = ps
        self.gs = gs
        house_built = False
        # Loop through all the streets
        for i in range(3):
            # Loop through all the homes in the street
            for j in range(len(self.ps.streets[i].homes)):
                curr_house: House = self.ps.streets[i].homes[j]
                # If the house is not built...
                if not curr_house.is_built:
                    excl_range = get_exclusive_range(self.ps.streets[i], j)
                    non_roundabout_excl_range = excl_range[0]
                    can_roundabout_be_played_in_gap = excl_range[1]
                    roundabout_excl_range = excl_range[2]
                    ## Check/Case: can a non-roundabout move be played
                    # If the difference between the returned "max" and "min" is equal to 1,
                    #   skip to the next street
                    if non_roundabout_excl_range[1] - non_roundabout_excl_range[0] != 1:
                        # If we're here, we know a valid range exists...
                        # If a construction card in gs can be played, play it. If it can't be played, continue.
                        house_built = self._play_construction_card_if_allowed(i, j, False, non_roundabout_excl_range)
                        if house_built:
                            # If a house was built, we've made our move--no need to continue looping.
                            break
                        ## Case: a non-roundabout move cannot be played
                        # verify that there is space for a roundabout to be played in the gap, and that the range is valid
                        if can_roundabout_be_played_in_gap and self.vm.get_total_num_roundabouts() < 2 and (roundabout_excl_range[1] - roundabout_excl_range[0] != 1):
                            # Play a roundabout if a cc exists for the computer valid gap range.
                            house_built = self._play_construction_card_if_allowed(i, j, True, roundabout_excl_range)
                            if house_built:
                                break

        if not house_built:
            # Increment refusals
            self.vm.refusals += 1
        ### Now self.vm is a PlayerState with the valid move (if there is one) played
        return self.vm
