import sys
sys.path.append('../../../')

class CityPlan:
    def __init__(self, inp_cp: dict):
        self.criteria: list = inp_cp.get("criteria")
        self.position: int = inp_cp.get("position")
        self.score1: int = inp_cp.get("score1")
        self.score2: int = inp_cp.get("score2")

    def return_literal(self):
        return {
            "criteria": self.criteria,
            "position": self.position,
            "score1": self.score1,
            "score2": self.score2
        }
