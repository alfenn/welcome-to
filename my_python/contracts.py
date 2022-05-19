import sys

sys.path.append('../../')


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
                and inp[1] == "bis"))


### Validators for Street ###

def pools_contract(inp) -> bool:
    # Check: type and length of "pools" input
    if not type(inp) == list and len(inp) == 3: return False
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


def player_contract(inp) -> bool:
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
