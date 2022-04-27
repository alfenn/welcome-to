from unittest import TestCase
from my_python.a3_1.PlayerState import *


class TestFailingPlayerState(TestCase):
    input_agents_g_1_robby = {"agents": [1, 0, 0, 0, 0, 0],
                              "city-plan-score": ["blank", "blank", "blank"],
                              "refusals": 0,
                              "streets":
                                  [
                                      {
                                          "homes": ["blank", False,
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False]],
                                          "parks": 0,
                                          "pools": [False, False, False]
                                      },
                                      {
                                          "homes": ["blank", False,
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False]],
                                          "parks": 0,
                                          "pools": [False, False, False]},
                                      {
                                          "homes": ["blank", False,
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False],
                                                    [False, "blank", False]],
                                          "parks": 0,
                                          "pools": [False, False, False]}
                                  ],
                              "temps": 0
                              }
    input_bis_b_1_robby = {
        "agents": [0, 0, 0, 0, 0, 0],
        "city-plan-score": ["blank", "blank", "blank"],
        "refusals": 0,
        "streets": [
            {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }, {
                "homes": [3, False,
                          [False, 4, False],
                          [False, [3, "bis"], False],
                          [False, 6, False],
                          [False, 7, False],
                          [False, 8, False],
                          [False, 9, False],
                          [False, 10, False],
                          [False, 11, False],
                          [False, 12, False],
                          [False, 13, False]],
                "parks": 0,
                "pools": [False, False, False]
            }, {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }
        ],
        "temps": 0
    }
    input_cityplan_g_1_robby = {
        "agents": [1, 0, 0, 0, 0, 0],
        "city-plan-score": [6, "blank", "blank"],
        "refusals": 0,
        "streets": [
            {"homes": ["blank", False,
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False]],
             "parks": 0,
             "pools": [False, False, False]},
            {"homes": ["blank", False,
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False]],
             "parks": 0,
             "pools": [False, False, False]},
            {"homes": ["blank", False,
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False]],
             "parks": 0,
             "pools": [False, False, False]}],
        "temps": 0}
    input_bis_b_4_robby = {
        "agents": [0, 0, 0, 0, 0, 0],
        "city-plan-score": ["blank", "blank", "blank"],
        "refusals": 0,
        "streets":
            [
                {
                    "homes": ["blank", False,
                              [False, 0, False],
                              [True, [0, "bis"], False],
                              [False, "blank", False],
                              [False, "blank", False],
                              [False, "blank", False],
                              [False, "blank", False],
                              [False, "blank", False],
                              [False, "blank", False],
                              [False, "blank", False]],
                    "parks": 0,
                    "pools": [False, False, False]
                }, {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }, {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }
            ],
        "temps": 0
    }
    input_bis_g_5_robby = {
        "agents": [0, 0, 0, 0, 0, 0],
        "city-plan-score": ["blank", "blank", "blank"],
        "refusals": 0,
        "streets":
            [
                {
                    "homes": ["blank", False,
                              [False, "blank", False],
                              [False, "blank", False],
                              [False, "blank", False],
                              [False, "blank", False],
                              [False, "blank", False],
                              [False, "blank", False],
                              [False, "blank", False],
                              [False, "blank", False],
                              [False, "blank", False]],
                    "parks": 0,
                    "pools": [False, False, False]
                }, {
                "homes": [3, False,
                          [False, 4, False],
                          [False, [4, "bis"], False],
                          [False, [4, "bis"], False],
                          [False, [7, "bis"], False],
                          [False, [7, "bis"], False],
                          [False, 7, False],
                          [False, 10, False],
                          [False, 11, False],
                          [False, 12, False],
                          [False, 13, False]],
                "parks": 0,
                "pools": [False, False, False]
            }, {
                "homes": ["blank", False,
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]],
                "parks": 0,
                "pools": [False, False, False]
            }
            ],
        "temps": 0}
    input_correct_2_test_team1 = {
        "agents": [
            0,
            0,
            0,
            0,
            0,
            0
        ],
        "city-plan-score": [
            "blank",
            "blank",
            "blank"
        ],
        "refusals": 0,
        "streets": [
            {
                "homes": [
                    "blank",
                    False,
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ]
                ],
                "parks": 0,
                "pools": [
                    False,
                    False,
                    False
                ]
            },
            {
                "homes": [
                    "blank",
                    False,
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ]
                ],
                "parks": 0,
                "pools": [
                    False,
                    False,
                    False
                ]
            },
            {
                "homes": [
                    "blank",
                    False,
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ],
                    [
                        True,
                        "blank",
                        False
                    ]
                ],
                "parks": 0,
                "pools": [
                    False,
                    False,
                    False
                ]
            }
        ],
        "temps": 0
    }

    def test_agents(self):
        ### self.assertTrue(PlayerState(self.input_agents_g_1_robby))
        ### self.assertRaises(AssertionError, lambda: PlayerState(self.input_bis_b_1_robby))
        ### self.assertRaises(AssertionError, lambda: PlayerState(self.input_bis_b_4_robby))
        ### self.assertTrue(PlayerState(self.input_bis_g_5_robby))
        ### self.assertTrue(PlayerState(self.input_cityplan_g_1_robby))
        self.assertTrue(PlayerState(self.input_correct_2_test_team1))
