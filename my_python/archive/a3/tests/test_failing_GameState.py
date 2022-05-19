from unittest import TestCase

city_plans_b_1_robby = \
    {
        "city-plans":
            [
                {
                    "criteria":[1,1,1,1,1,1],
                    "position":1,
                    "score1":8,
                    "score2":4
                },
                {
                    "criteria":[6,1,2],
                    "position":3,
                    "score1":12,
                    "score2":7
                },
                {
                    "criteria":[1,1,1,6],
                    "position":2,
                    "score1":11,
                    "score2":6
                }
            ],
        "city-plans-won":[False,False,False],
        "construction-cards":[[1,"surveyor"],
                              [2,"landscaper"],
                              [3,"pool"]],
        "effects":["agent","bis","temp"]
    }

input_basics_g_1_robby = \
    {
        "city-plans":
            [
                {
                    "criteria":[1,1,1,1,1,1],
                    "position":1,
                    "score1":8,
                    "score2":4
                },
                {
                    "criteria":[1,1,1,6],
                    "position":2,
                    "score1":11,
                    "score2":6},
                {
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
        "effects":["agent","bis","temp"]
    }

input_city_plan_b_7_robby = \
    {
        "city-plans":
            [
                {
                    "criteria":[1,1,1,1,1,1],
                    "position":1,
                    "score1":8,
                    "score2":4
                },
                {
                    "criteria":[1,2,6],
                    "position":3,
                    "score1":12,
                    "score2":7},
                {
                    "criteria":[1,1,1,6],
                    "position":1,
                    "score1":11,
                    "score2":6
                }
            ],
        "city-plans-won":[False,False,False],
        "construction-cards":
            [
                [1,"surveyor"],[2,"landscaper"],[3,"pool"]
            ],
        "effects":["agent","bis","temp"]
    }

input_incorrect_4_team1 = \
    {
      "city-plans": [
        {
          "criteria": [
            1,
            1,
            1,
            1,
            1,
            1
          ],
          "position": 1,
          "score1": 8,
          "score2": 4
        },
        {
          "criteria": [
            1,
            1,
            1,
            6
          ],
          "position": 2,
          "score1": 11,
          "score2": 6
        },
        {
          "criteria": [
            1,
            2,
            6
          ],
          "position": 3,
          "score1": 12,
          "score2": 7
        }
      ],
      "city-plans-won": [
        False,
        False,
        False
      ],
      "construction-cards": [
        [
          18014398509481985,
          "surveyor"
        ],
        [
          2,
          "landscaper"
        ],
        [
          3,
          "pool"
        ]
      ],
      "effects": [
        "agent",
        "bis",
        "temp"
      ]
    }

correct_4_team1 = \
    {
        "city-plans": [
            {
                "criteria": [],
                "position": 1,
                "score1": 8,
                "score2": 4
            },
            {
                "criteria": [
                    1,
                    1,
                    1,
                    6
                ],
                "position": 2,
                "score1": 11,
                "score2": 6
            },
            {
                "criteria": [
                    1,
                    15,
                    15
                ],
                "position": 3,
                "score1": 12,
                "score2": 76
            }
        ],
        "city-plans-won": [
            False,
            False,
            False
        ],
        "construction-cards": [
            [
                15,
                "surveyor"
            ],
            [
                15,
                "landscaper"
            ],
            [
                15,
                "pool"
            ]
        ],
        "effects": [
            "agent",
            "bis",
            "temp"
        ]
    }

class TestFailingGameState(TestCase):
    def test_inputs(self):
        self.assertRaises(AssertionError, lambda: GameState(city_plans_b_1_robby))
        self.assertTrue(GameState(input_basics_g_1_robby))
        self.assertRaises(AssertionError, lambda: GameState(input_city_plan_b_7_robby))
        self.assertRaises(AssertionError, lambda: GameState(input_incorrect_4_team1))
        self.assertTrue(GameState(correct_4_team1))