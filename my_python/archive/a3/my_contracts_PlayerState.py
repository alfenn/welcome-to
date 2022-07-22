from contracts import *
from contracts import new_contract

def check_wrapper(s: str, v) -> bool:
    try:
        check(s, v)
        return True
    except:
        return False


#################################
## Define the LocalPlayer contracts ##
#################################

#### Contracts for House ####
valid_natural = new_contract('valid_natural', lambda n: ((isinstance(n, int)
                                                         and 0 <= n)
                                                         or n == "same"))
valid_nb = new_contract('valid_nb', lambda nb: (check_wrapper('valid_natural', nb)
                                                or nb == "blank"))
valid_bis = new_contract('valid_bis', lambda b: (isinstance(b, list)
                                                 and len(b) == 2
                                                 and check_wrapper('valid_natural', b[0])
                                                 and b[1] == "bis"))
valid_house = new_contract('valid_house', lambda h: ((check_wrapper('valid_bis', h)
                                                     or check_wrapper('valid_nb', h))
                                                    or h == "same"))

#### Contracts for Homes ####
valid_fence = new_contract('valid_fence', bool)
valid_used_in_plan = new_contract('valid_used_in_plan', bool)
valid_parks = new_contract('valid_parks', 'valid_natural')
valid_pools = new_contract('valid_pools', lambda l: (isinstance(l, list)
                                                     and len(l) == 3
                                                     and isinstance(l[0], bool)
                                                     and isinstance(l[1], bool)
                                                     and isinstance(l[2], bool)))

#### Contracts for homes ####
valid_homes_val_list = new_contract('valid_homes_val_list', lambda l: (isinstance(l, list)
                                                                       and len(l) == 3
                                                                       and check_wrapper('valid_fence', l[0])
                                                                       and check_wrapper('valid_house', l[1])
                                                                       and check_wrapper('valid_used_in_plan', l[2])))


def valid_homes_ind_ge_2_check_wrapper(l):
    for i in range(len(l) - 2):
        i += 2
        try:
            check_wrapper('valid_homes_val_list', l[i])
        except:
            return False
    return True


valid_homes = new_contract('valid_homes', lambda l: (isinstance(l, list)
                                                     and 11 <= len(l) <= 13
                                                     and check_wrapper('valid_house', l[0])
                                                     and check_wrapper('valid_used_in_plan', l[1])
                                                     and valid_homes_ind_ge_2_check_wrapper(l)))

#### Contracts for street ####
valid_street = new_contract('valid_street', lambda d: (isinstance(d, dict)
                                                       and d.keys() == {"homes": None,
                                                                        "parks": None,
                                                                        "pools": None}.keys()
                                                       and check_wrapper('valid_homes', d.get("homes"))
                                                       and check_wrapper('valid_natural', d.get("parks"))
                                                       and check_wrapper('valid_pools', d.get("pools"))))

#### Contracts for the LocalPlayer state ####
valid_temps = new_contract('valid_temps', 'valid_natural')
valid_streets = new_contract('valid_streets', 'list[3](valid_street)')
valid_refusals = new_contract('valid_refusals', 'valid_natural')
valid_city_plan_score = new_contract('valid_city_plan_score', 'list[3](valid_nb)')
valid_agents = new_contract('valid_agents', 'list(valid_natural)')
valid_player_state = new_contract('valid_player_state', lambda d: (isinstance(d, dict)
                                                                   and len(d) == 5
                                                                   and d.keys() == {"agents": None,
                                                                                    "city-plan-score": None,
                                                                                    "refusals": None,
                                                                                    "streets": None,
                                                                                    "temps": None}.keys()
                                                                   and check_wrapper('valid_agents', d.get("agents"))
                                                                   and check_wrapper('valid_city_plan_score',
                                                                                     d.get("city-plan-score"))
                                                                   and check_wrapper('valid_refusals',
                                                                                     d.get("refusals"))
                                                                   and check_wrapper('valid_streets', d.get("streets"))
                                                                   and check_wrapper('valid_temps', d.get("temps"))))
