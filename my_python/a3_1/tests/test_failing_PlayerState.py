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
    def test_agents(self):
        self.assertTrue(PlayerState(self.input_agents_g_1_robby))
