import sys, json
from typing import List

sys.path.append('../../../')
from my_python.contracts import gamestate_contract
from my_python.exceptions import InvalidGameState
from my_python.CityPlan import CityPlan

class GameState:
    def __init__(self, inp_gs):
        self.city_plans: List[CityPlan] = []
        self.city_plans_won: List[bool] = []
        self.construction_cards: list = []
        self.effects = []
        gamestate_contract(inp_gs)
        # Initialize the class members
        for cp in inp_gs["city-plans"]:
            self.city_plans.append(CityPlan(cp))
        self.city_plans_won = inp_gs["city-plans-won"]
        self.construction_cards = inp_gs["construction-cards"]
        self.effects = inp_gs["effects"]
        
    def __str__(self):
        ret = {
            "city-plans": [],
            "city-plans-won": self.city_plans_won,
            "construction-cards": self.construction_cards,
            "effects": self.effects
        }
        for cp in self.city_plans:
            ret["city-plans"].append(cp.return_literal())
        return json.dumps(ret)
