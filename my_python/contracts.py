import sys

sys.path.append('../../')
from my_python.exceptions import InvalidGameState

####################################################################################################
######################### Validators for various PlayerState subclasses ############################
####################################################################################################
### Basic validators and validators for House ###

def natural_contract(inp) -> bool:
    return type(inp) == int and inp >= 0

def nb_contract(inp) -> bool:
    return natural_contract(inp) or inp == "blank"

## My own validator definitions
def house_num_contract(inp) -> bool:
    return natural_contract(inp) and inp <= 17


######################################
####### House wrapper contract #######
######################################
def house_contract(inp) -> bool:
    return (house_num_contract(inp)  # Case 1: num
            or inp == "blank"  # Case 2: "blank"
            or (type(inp) == list  # Case 3: [num, "bis"]
                and len(inp) == 2
                and house_num_contract(inp[0])
                and inp[1] == "bis")
            or inp == "roundabout")

### Validators for Street ###

def pools_contract(inp) -> bool:
    # Check: type and length of "pools" input
    if not (type(inp) == list and len(inp) == 3): return False
    for i in range(3):
        if not (type(inp[i]) == bool): return False
    return True

def homes_contract(inp) -> bool:
    # Check: type and length of "homes" input
    if not (type(inp) == list and 11 <= len(inp) <= 13): return False
    for i in range(len(inp)):
        # Case: validate the first house
        if i == 0 or i == 1:
            if not (house_contract(inp[0]) and type(inp[1]) == bool): return False
        # Case: validate non-first homes (aka. [fence-or-not, house, used-in-plan])
        else:
            curr_elem = inp[i]
            if not (type(curr_elem) == list
                    and len(curr_elem) == 3
                    and type(curr_elem[0]) == bool
                    and house_contract(curr_elem[1])
                    and type(curr_elem[2]) == bool):
                return False
    return True


#######################################
####### Street wrapper contract #######
#######################################
def street_contract(inp) -> bool:
    ## Check: format of input
    return (type(inp) == dict  # Check: dict, and dict keys
            and sorted(list(inp.keys())) == sorted(["homes", "parks", "pools"])
            and homes_contract(inp["homes"])  # Check: "homes" format
            and natural_contract(inp["parks"])  # Check: "parks" format
            and pools_contract(inp["pools"]))  # Check: "pools" format


############################################
####### PlayerState wrapper contract #######
############################################
def agents_contract(inp) -> bool:
    valid_agent_values = [1, 2, 3, 4, 4, 4]
    # Case: type of agents value is not a list of length 6
    if not (type(inp) == list and len(inp) == 6): return False
    for i in range(6):
        curr_agent = inp[i]
        if not (natural_contract(curr_agent)  # Case: agent value is not a natural number
                and curr_agent <= valid_agent_values[i]):  # Case: agent value is not smaller than max allowed value
            return False
    return True

def city_plan_score_contract(inp) -> bool:
    # Case: input of city-plan-score value is not an array of length 3
    if not (type(inp) == list and len(inp) == 3): return False
    for i in range(3):
        curr_score = inp[i]
        if not (nb_contract(curr_score)): return False  # Case: city-plan-score value is not an nb
    return True

def refusals_contract(inp) -> bool:
    # Check: input must be a natural that is less than or equal to 3
    return natural_contract(inp) and inp <= 3

def temps_contract(inp) -> bool:
    # Case: input needs to be a natural and be between [0,11]
    if not (natural_contract(inp) and 0 <= inp <= 11): return False
    return True

def streets_contract(inp) -> bool:
    valid_street_lengths = [10, 11, 12]
    # Check: input is a list of length 3
    if not (type(inp) == list and len(inp) == 3): return False
    # Check: first street is length 10, ...
    for i in range(3):
        curr_street = inp[i]
        if not street_contract(curr_street): return False
        if not (len(curr_street["homes"]) == valid_street_lengths[i] + 1): return False
    return True

def playerstate_contract(inp) -> bool:
    # Check: the type is dict and all the keys are present
    if not (type(inp) == dict
            and sorted(list(inp.keys())) == sorted(["agents", "city-plan-score", "refusals", "streets", "temps"])):
        return False
    if (not agents_contract(inp["agents"])
            or not city_plan_score_contract(inp["city-plan-score"])
            or not refusals_contract(inp["refusals"])
            or not streets_contract(inp["streets"])
            or not temps_contract(inp["temps"])): return False
    return True


####################################################################################################
######################### Validators for various GameState subclasses ##############################
####################################################################################################
def effect_contract_b(e) -> bool:
    valid_effects = [
        "surveyor",
        "agent",
        "landscaper",
        "pool",
        "temp",
        "bis"
    ]
    return e in valid_effects

def effects_contract(effs) -> None:
    if not (type(effs) == list and len(effs) == 3):
        raise InvalidGameState('"effects" must be a list of length 3')
    for e in effs:
        if not effect_contract_b(e):
            raise InvalidGameState('Each element of "effects" must be a valid effect')

#### Construction card contracts
def construction_card_contract(c) -> None:
    if (not (type(c) == list and len(c) == 2)
            or not (natural_contract(c[0]) and 1 <= c[0] <= 15)
            or not effect_contract_b(c[1])):
        raise InvalidGameState('Each element of "construction-cards" must be [natural, effect]')

def construction_cards_list_contract(inp: list) -> None:
    if not (type(inp) == list and len(inp) == 3):
        raise InvalidGameState('"construction-cards" must be a list of length 3')
    for c in inp:
        construction_card_contract(c)

def city_plans_won_contract(inp: list) -> None:
    if not (type(inp) == list and len(inp) == 3):
        raise InvalidGameState('"city-plans-won" must be a list of length 3')
    for el in inp:
        if not type(el) == bool:
            raise InvalidGameState('Each element of "city-plans-won" must be a bool')

##########################################
####### CityPlan wrapper contracts #######
##########################################
ACCEPTABLE_CRITERIA_CARD_1S = [
            ["all houses", 0],
            ["all houses", 2],
            "end houses",
            "7 temps",
            "5 bis"
]
ACCEPTABLE_CRITERIA_CARD_2S = [
            "two streets all parks",
            "two streets all pools",
            ["all pools all parks", 1],
            ["all pools all parks", 2],
            "all pools all parks one roundabout"
]

def position_contract(pos: int) -> None:
    if not (1 <= pos <= 3): raise InvalidGameState("Position must either be 1, 2, or 3")

def criteria_contract(cri, pos: int) -> None:
    def _natural_sorted_list_contract_b(cri) -> bool:
        """
        Return True if `cri` is a List[natural] and False otherwise.
        """
        if not type(cri) == list:
            return False
        for nat in cri:
            if natural_contract(nat) is False:
                return False
        if sorted(cri) != cri:
            return False
        return True
    def _criteria_card_1_contract_b(cri) -> bool:
        return cri in ACCEPTABLE_CRITERIA_CARD_1S
    def _criteria_card_2_contract_b(cri) -> bool:
        return cri in ACCEPTABLE_CRITERIA_CARD_2S
    # City plans in position 1: must have "criteria" that is either List[natural] or criteria-card-1
    if pos == 1:
        if not (_natural_sorted_list_contract_b(cri) or _criteria_card_1_contract_b(cri)):
            raise InvalidGameState('City plans in position 1 must have "criteria" that is either a sorted List[natural] or criteria-card-1')
    # City plans in position 2: must have "criteria" that is either List[natural] or criteria-card-2
    elif pos == 2:
        if not (_natural_sorted_list_contract_b(cri) or _criteria_card_2_contract_b(cri)):
            raise InvalidGameState('City plans in position 2 must have "criteria" that is either a sorted List[natural] or criteria-card-2')
    # City plans in position 1: must have "criteria" that iscan be only List[natural]
    else:   # pos == 3
        if not (_natural_sorted_list_contract_b(cri)):
            raise InvalidGameState('City plans in position 3 must have "criteria" that is a sorted List[natural]')

def city_plan_contract(cp: dict):
    # Check: the type is a dict and all the keys are present
    if not (type(cp) == dict and sorted(list(cp.keys())) == sorted(["criteria", "position", "score1", "score2"])):
        raise InvalidGameState('Each element of "city-plans" must be a dictionary containing exactly the following keys: "criteria", "position", "score1", "score2"')
    position_contract(cp["position"])
    criteria_contract(cp["criteria"], cp["position"])
    if not natural_contract(cp["score1"]):
        raise InvalidGameState('Each "city-plans" element\'s "score1" value must be a natural')
    if not natural_contract(cp["score2"]):
        raise InvalidGameState('Each "city-plans" element\'s "score2" value must be a natural')

def city_plans_list_contract(inp: list):
    def _positions_unique_contract(inp: list) -> None:
        """
        Makes sure that there is one city plan for each position (1,2,3)
        """
        all_positions = []
        for cp in inp:
            all_positions.append(cp["position"])
        if not (sorted(all_positions) == [1,2,3]):
            raise InvalidGameState('"city-plans" must have elements with positions 1, 2, 3')
    # Check: length of the input
    if not (type(inp) == list and len(inp) == 3):
        raise InvalidGameState('"city-plans" must be a list of length 3')
    for cp in inp:
        city_plan_contract(cp)
    _positions_unique_contract(inp)

def gamestate_contract(inp: dict) -> None:
    # Check: the type is dict and all the keys are present
    if not (type(inp) == dict
            and sorted(list(inp.keys())) == sorted(["city-plans", "city-plans-won", "construction-cards", "effects"])):
        raise InvalidGameState('GameState must be initialized with a dictionary containing exactly following keys: "city-plans", "city-plans-won", "construction-cards", "effects"')
    # Check: the subcontracts
    city_plans_list_contract(inp["city-plans"])
    city_plans_won_contract(inp["city-plans-won"])
    construction_cards_list_contract(inp["construction-cards"])
    effects_contract(inp["effects"])
