###############################
## Define the Game contracts ##
###############################
def validate_natural(nat) -> bool:
    assert isinstance(nat, int) \
           and not isinstance(nat, bool) \
           and nat >= 0, \
        "natural must be an integer geq 0"
    return True


def validate_effect(eff) -> bool:
    assert type(eff) == str, "effect must be a string"
    poss_effects = ["surveyor", "agent", "landscaper", "pool", "temp", "bis"]
    assert poss_effects.count(eff) > 0, 'effect must be either "surveyor", "agent", "landscaper", "pool", "temp", "bis"'
    return True


def validate_construction_card(card) -> bool:
    assert len(card) == 2 \
           and (validate_natural(card[0])
                and 1 <= card[0] <= 15) \
           and validate_effect(card[1]), \
        "a construction card must be a [natural [1,15],effect]"
    return True


def validate_criteria(cri) -> bool:
    ## Check if it satisfies the criteria-card-1 non-terminal
    ## Check if it satisfies the
    if type(cri) == list:
        for ea in cri:
            try:
                validate_natural(ea)
            except:
                raise AssertionError("each element in the criteria array must be a valid natural")
    return True


def validate_position(pos) -> bool:
    assert (isinstance(pos, int)
            and not isinstance(pos, bool)) \
           and (pos == 1 or pos == 2 or pos == 3), \
        "a position must be 1, 2, or 3"
    return True

