from archive.OldCityPlan import *

class OldGameState:
    def __init__(self, in_gs):
        """
            Initialize the OldGameState structure
            :param in_gs: dict representing a city plan
        """
        ## Validate keys
        assert in_gs.keys() == {"city-plans":None,
                                "city-plans-won":None,
                                "construction-cards":None,
                                "effects":None}.keys(), \
            'keys of the game-state dict must be "city-plans", "city-plans-won", "construction-cards", "effects"'

        ## Validate city-plans
        assert isinstance(in_gs.get("city-plans"), list) \
               and len(in_gs.get("city-plans")) == 3, \
            "city-plans in game-state dict must be list of length == 3"
        for i in range(len(in_gs.get("city-plans"))):
            try:
                OldCityPlan(in_gs.get("city-plans")[i])
            except: raise AssertionError(
                "ind " + str(i) + " city-plans in game-state dict is not valid")
        # Ensure that there is only one 1,2, and 3 in position
        city_plan_positions = []
        for i in range(len(in_gs.get("city-plans"))):
            city_plan_positions.append(in_gs.get("city-plans")[i].get("position"))
        assert sorted(city_plan_positions) == [1,2,3], "city-plans must have positions that are exactly 1,2,3"

        ## Validate city-plans-won
        assert isinstance(in_gs.get("city-plans-won"), list) \
               and len(in_gs.get("city-plans-won")) == 3, \
            "city-plans-won must be of type list and must have length == 3"
        for i in range(len(in_gs.get("city-plans-won"))):
            assert isinstance(in_gs.get("city-plans-won")[i], bool), \
                "ind " + str(i) + " city-plans-won in game-state dict is not valid"

        ## Validate construction-cards
        assert isinstance(in_gs.get("construction-cards"), list) \
               and len(in_gs.get("construction-cards")) == 3, \
            "construction-cards in game-state dict must be list with length == 3"
        for i in range(len(in_gs.get("construction-cards"))):
            try: validate_construction_card(in_gs.get("construction-cards")[i])
            except: raise AssertionError("ind " + str(i) + " construction-cards in game-state dict is not valid")

        ## Validate effects
        assert isinstance(in_gs.get("effects"), list) \
               and len(in_gs.get("effects")) == 3, \
            "effects in game-state dict must be list with length == 3"
        for i in range(len(in_gs.get("effects"))):
            try: validate_effect(in_gs.get("effects")[i])
            except: raise AssertionError("ind " + str(i) + " effects in game-state dict is not valid")

        ######################## Initialize fields
        self.city_plans = []
        for ea in in_gs.get("city-plans"):
            self.city_plans.append(OldCityPlan(ea))

        self.city_plans_won = []
        for ea in in_gs.get("city-plans-won"):
            self.city_plans_won.append(ea)

        self.construction_cards = []
        for ea in in_gs.get("construction-cards"):
            # each construction card is just a [num, effect] list
            #  we did not create a class
            self.construction_cards.append(ea)

        self.effects = []
        for ea in in_gs.get("effects"):
            self.effects.append(ea)

