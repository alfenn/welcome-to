from archive.my_contracts_OldGameState import *
class OldCityPlan:
    def __init__(self, in_cp: dict):
        """
            Initialize OldCityPlan object
            :param in_cp: dict representing a city plan
        """
        ## Validate keys
        assert in_cp.keys() == {"criteria":None,
                                "position":None,
                                "score1":None,
                                "score2":None}.keys(), \
            'keys of the city-plan dict must be "criteria", "position", "score1", "score2"'
        ## Validate criteria
        try: validate_criteria(in_cp.get("criteria"))
        except: raise AssertionError("criteria in city-plan dict is not valid")
        ## Validate that the criteria scores are in sorted order
        assert in_cp.get("criteria") == sorted(in_cp.get("criteria")), "criteria elements aren't sorted"
        ## Validate position
        try: validate_position(in_cp.get("position"))
        except: raise AssertionError("position in city-plan dict is not valid")
        ## Validate score1
        try: validate_natural(in_cp.get("score1"))
        except: raise AssertionError("score1 in city-plan dict is not valid")
        ## Validate score2
        try: validate_natural(in_cp.get("score2"))
        except: raise AssertionError("score2 in city-plan dict is not valid")

        ######################## Initialize fields
        self.criteria: list = in_cp.get("criteria")
        self.position: int = in_cp.get("position")
        self.score1: int = in_cp.get("score1")
        self.score2: int = in_cp.get("score2")
