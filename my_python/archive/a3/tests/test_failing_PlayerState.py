from unittest import TestCase
from my_python.archive.a3.PlayerState import *


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
    test_assert_line17_homes = {"agents": [1, 0, 0, 0, 0, 0],
                              "city-plan-score": ["blank", "blank", "blank"],
                              "refusals": 0,
                              "streets":
                                  [
                                      {
                                          "homes": ["blank", False,
                                                    [0, "blank", False],
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
    input_row_count_b_10_robby = {
        "agents":[0,0,0,0,0,0],
        "city-plan-score":["blank","blank","blank"],
        "refusals":0,
        "streets":
            [
                {
                    "homes":
                        ["blank",False,
                         [False,"blank",False],
                         [False,"blank",False],
                         [False,"blank",False],
                         [False,"blank",False],
                         ["wrong","blank",False],
                         [False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False]],"parks":0,"pools":[False,False,False]},{"homes":["blank",False,[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False]],"parks":0,"pools":[False,False,False]},{"homes":["blank",False,[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False]],"parks":0,"pools":[False,False,False]}],"temps":0}
    input_incorrect_3_team_1 = {
  "agents": [
    False,
    False,
    False,
    False,
    False,
    False
  ],
  "city-plan-score": [
    "blank",
    "blank",
    "blank"
  ],
  "refusals": False,
  "streets": [
    {
      "homes": [
        False,
        False,
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ]
      ],
      "parks": False,
      "pools": [
        False,
        False,
        False
      ]
    },
    {
      "homes": [
        False,
        False,
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ]
      ],
      "parks": False,
      "pools": [
        False,
        False,
        False
      ]
    },
    {
      "homes": [
        False,
        False,
        [
          False,
          True,
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ]
      ],
      "parks": False,
      "pools": [
        False,
        False,
        False
      ]
    }
  ],
  "temps": False
}
    input18_team10_exp_False = {
  "agents": [0, 0, 0, 0, 0, 0],
  "city-plan-score": ["blank", "blank", "blank"],
  "refusals": 0,
  "streets": [
    {
      "homes": [
        "blank",
        False,
        [False, "blank", False, True],
        [False, "blank", False],
        [False, "blank", False],
        [False, "blank", False],
        [False, "blank", False],
        [False, "blank", False],
        [False, "blank", False],
        [False, "blank", False],
        [False, "blank", False]
      ],
      "parks": 0,
      "pools": [False, False, False]
    },
    {
      "homes": [
        "blank",
        False,
        [False, "blank", False],
        [False, "blank", False],
        [False, "blank", False],
        [False, "blank", False],
        [False, "blank", False],
        [False, "blank", False],
        [False, "blank", False],
        [False, "blank", False],
        [False, "blank", False],
        [False, "blank", False]
      ],
      "parks": 0,
      "pools": [False, False, False]
    },
    {
      "homes": [
        "blank",
        False,
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
        [False, "blank", False]
      ],
      "parks": 0,
      "pools": [False, False, False]
    }
  ],
  "temps": 0
}
    input17_team19 = {
        "agents":[0,1,0,2,0,4],
        "city-plan-score":
            ["blank",6,7],
        "refusals":1,
        "streets":
            [
                {
                    "homes":[True,False,
                             [True,2,True],
                             [False,3,True],
                             [False,4,True],
                             [True,5,False],
                             [False,6,False],
                             [False,7,False],
                             [False,8,False],
                             [False,9,False],
                             [False,10,False]],
                    "parks":2,
                    "pools":[False,True,True]},
                {
                    "homes":[0,False,
                          [False,1,False],
                          [True,2,False],
                          [False,[2,"bis"],False],
                          [False,"blank",False],
                          [False,[6,"bis"],False],
                          [False,6,False],
                          [True,10,False],
                          [False,"blank",False],
                          [False,12,False],
                          [False,16,False]],
                    "parks":1,
                    "pools":[True,False,False]
                },{
                    "homes":[1,False,
                             [False,2,False],
                             [True,3,False],
                             [True,4,True],
                             [True,5,True],
                             [True,6,True],
                             [True,7,False],
                             [False,8,False],
                             [False,9,False],
                             [False,10,False],
                             [False,11,False],
                             [False,12,False]],
                    "parks":5,
                    "pools":[False,False,False]
                }
            ],
        "temps":4
    }

    input15_team2 = {
        "agents":[0,0,0,0,0,True],
        "city-plan-score":["blank","blank","blank"],"refusals":0,"streets":[{"homes":["blank",False,[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False]],"parks":0,"pools":[False,False,False]},{"homes":["blank",False,[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False]],"parks":0,"pools":[False,False,False]},{"homes":["blank",False,[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False],[False,"blank",False]],"parks":0,"pools":[False,False,False]}],"temps":0}
    input_correct_6_test_team1 = {
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
        [0, "bis"],
        False,
        [
          False,
          0,
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          17,
          False
        ],
        [
          False,
          [17, "bis"],
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
        [2, "bis"],
        False,
        [
          False,
          2,
          False
        ],
        [
          False,
          [2, "bis"],
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          15,
          False
        ],
        [
          False,
          [15, "bis"],
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
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
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
          "blank",
          False
        ],
        [
          False,
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
        self.assertTrue(PlayerState(self.input_agents_g_1_robby))
        self.assertRaises(AssertionError, lambda: PlayerState(self.input_bis_b_1_robby))
        self.assertRaises(AssertionError, lambda: PlayerState(self.input_bis_b_4_robby))
        self.assertTrue(PlayerState(self.input_bis_g_5_robby))
        self.assertTrue(PlayerState(self.input_cityplan_g_1_robby))
        self.assertTrue(PlayerState(self.input_correct_2_test_team1))
        self.assertRaises(AssertionError, lambda: PlayerState(self.input_row_count_b_10_robby))
        self.assertRaises(AssertionError, lambda: PlayerState(self.test_assert_line17_homes))
        self.assertRaises(AssertionError, lambda: PlayerState(self.input_incorrect_3_team_1))
        self.assertRaises(AssertionError, lambda: PlayerState(self.input18_team10_exp_False))
        self.assertRaises(AssertionError, lambda: PlayerState(self.input15_team2))
        self.assertRaises(AssertionError, lambda: PlayerState(self.input17_team19))
        self.assertTrue(PlayerState(self.input_correct_6_test_team1))