from unittest import TestCase

spec_valid = {
    "city-plans":
        [
            {
                "criteria":[1,1,1,1,1,1],
                "position":1,
                "score1":8,
                "score2":4
            },{
                "criteria":[1,1,1,6],
                "position":2,
                "score1":11,
                "score2":6
            },{
                "criteria":[1,2,6],
                "position":3,
                "score1":12,
                "score2":7
            }
        ],
    "city-plans-won":[False,False,False],
    "construction-cards":
        [
            [1,"surveyor"],
            [2,"landscaper"],
            [3,"pool"]
        ],
    "effects": ["agent","bis","temp"]
}

city_plans_invalid_bool = {
    "city-plans":
        [
            False
            ,{
                "criteria":[1,1,1,6],
                "position":2,
                "score1":11,
                "score2":6
            },{
                "criteria":[1,2,6],
                "position":3,
                "score1":12,
                "score2":7
            }
        ],
    "city-plans-won":[False,False,False],
    "construction-cards":
        [
            [1,"surveyor"],
            [2,"landscaper"],
            [3,"pool"]
        ],
    "effects": ["agent","bis","temp"]
}

city_plans_invalid_len = {
    "city-plans":
        [
            {
                "criteria":[1,1,1,1,1,1],
                "position":1,
                "score1":8,
                "score2":4
            },{
                "criteria":[1,1,1,6],
                "position":2,
                "score1":11,
                "score2":6
            },{
                "criteria":[1,2,6],
                "position":3,
                "score1":12,
                "score2":7
            },{
                "criteria":[1,2,6],
                "position":3,
                "score1":12,
                "score2":7
            }
        ],
    "city-plans-won":[False,False,False],
    "construction-cards":
        [
            [1,"surveyor"],
            [2,"landscaper"],
            [3,"pool"]
        ],
    "effects": ["agent","bis","temp"]
}

construction_cards_invalid_num = {
    "city-plans":
        [
            {
                "criteria":[1,1,1,1,1,1],
                "position":1,
                "score1":8,
                "score2":4
            },{
                "criteria":[1,1,1,6],
                "position":2,
                "score1":11,
                "score2":6
            },{
                "criteria":[1,2,6],
                "position":3,
                "score1":12,
                "score2":7
            },{
                "criteria":[1,2,6],
                "position":3,
                "score1":12,
                "score2":7
            }
        ],
    "city-plans-won":[False,False,False],
    "construction-cards":
        [
            ["1","surveyor"],
            [2,"landscaper"],
            [3,"pool"]
        ],
    "effects": ["agent","bis","temp"]
}

construction_cards_invalid_effect = {
    "city-plans":
        [
            {
                "criteria":[1,1,1,1,1,1],
                "position":1,
                "score1":8,
                "score2":4
            },{
                "criteria":[1,1,1,6],
                "position":2,
                "score1":11,
                "score2":6
            },{
                "criteria":[1,2,6],
                "position":3,
                "score1":12,
                "score2":7
            },{
                "criteria":[1,2,6],
                "position":3,
                "score1":12,
                "score2":7
            }
        ],
    "city-plans-won":[False,False,False],
    "construction-cards":
        [
            [1,"yahoo"],
            [2,"landscaper"],
            [3,"pool"]
        ],
    "effects": ["agent","bis","temp"]
}

construction_cards_invalid_len = {
    "city-plans":
        [
            {
                "criteria":[1,1,1,1,1,1],
                "position":1,
                "score1":8,
                "score2":4
            },{
                "criteria":[1,1,1,6],
                "position":2,
                "score1":11,
                "score2":6
            },{
                "criteria":[1,2,6],
                "position":3,
                "score1":12,
                "score2":7
            },{
                "criteria":[1,2,6],
                "position":3,
                "score1":12,
                "score2":7
            }
        ],
    "city-plans-won":[False,False,False],
    "construction-cards":
        [
            [1,"surveyor"],
            [2,"landscaper"],
            [3,"pool"],
            [1,"landscaper"]
        ],
    "effects": ["agent","bis","temp"]
}

effects_invalid_effect = {
    "city-plans":
        [
            {
                "criteria":[1,1,1,1,1,1],
                "position":1,
                "score1":8,
                "score2":4
            },{
                "criteria":[1,1,1,6],
                "position":2,
                "score1":11,
                "score2":6
            },{
                "criteria":[1,2,6],
                "position":3,
                "score1":12,
                "score2":7
            },{
                "criteria":[1,2,6],
                "position":3,
                "score1":12,
                "score2":7
            }
        ],
    "city-plans-won":[False,False,False],
    "construction-cards":
        [
            [1,"surveyor"],
            [2,"landscaper"],
            [3,"pool"]
        ],
    "effects": ["agent","bis","temperamental"]
}

effects_invalid_effect_int = {
    "city-plans":
        [
            {
                "criteria":[1,1,1,1,1,1],
                "position":1,
                "score1":8,
                "score2":4
            },{
                "criteria":[1,1,1,6],
                "position":2,
                "score1":11,
                "score2":6
            },{
                "criteria":[1,2,6],
                "position":3,
                "score1":12,
                "score2":7
            },{
                "criteria":[1,2,6],
                "position":3,
                "score1":12,
                "score2":7
            }
        ],
    "city-plans-won":[False,False,False],
    "construction-cards":
        [
            [1,"surveyor"],
            [2,"landscaper"],
            [3,"pool"]
        ],
    "effects": ["agent","bis",1]
}

effects_invalid_effect_len = {
    "city-plans":
        [
            {
                "criteria":[1,1,1,1,1,1],
                "position":1,
                "score1":8,
                "score2":4
            },{
                "criteria":[1,1,1,6],
                "position":2,
                "score1":11,
                "score2":6
            },{
                "criteria":[1,2,6],
                "position":3,
                "score1":12,
                "score2":7
            },{
                "criteria":[1,2,6],
                "position":3,
                "score1":12,
                "score2":7
            }
        ],
    "city-plans-won":[False,False,False],
    "construction-cards":
        [
            [1,"surveyor"],
            [2,"landscaper"],
            [3,"pool"]
        ],
    "effects": ["agent","bis","bis","bis"]
}

class TestGameState(TestCase):
    def test_contracts(self):
        self.assertTrue(GameState(spec_valid))
        self.assertRaises(AssertionError, lambda: GameState(city_plans_invalid_bool))
        self.assertRaises(AssertionError, lambda: GameState(city_plans_invalid_len))
        self.assertRaises(AssertionError, lambda: GameState(construction_cards_invalid_num))
        self.assertRaises(AssertionError, lambda: GameState(construction_cards_invalid_effect))
        self.assertRaises(AssertionError, lambda: GameState(construction_cards_invalid_len))
        self.assertRaises(AssertionError, lambda: GameState(effects_invalid_effect))
        self.assertRaises(AssertionError, lambda: GameState(effects_invalid_effect_int))
        self.assertRaises(AssertionError, lambda: GameState(effects_invalid_effect_len))
