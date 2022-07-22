import sys
from collections import Counter

sys.path.append('../../')
from unittest import TestCase
from my_python.validate_move import *
from my_python.PlayerState import PlayerState
from my_python.exceptions import *
from my_python.tests.input_test_validate_move import *


class TestValidateMove(TestCase):
    """Unit testing for helpers in validate_move()"""

    def test_get_claimed_estates(self):
        self.assertEqual(get_claimed_estates(PlayerState(inp_ps=gs_ps_ps_house_num[1]),
                                             PlayerState(inp_ps=gs_ps_ps_house_num[2])),
                         [Counter(), False])
        self.assertEqual(get_claimed_estates(PlayerState(inp_ps=gs_ps_ps_invalid[1]),
                                             PlayerState(inp_ps=gs_ps_ps_invalid[2])),
                         [Counter(), False])
        self.assertEqual(get_claimed_estates(PlayerState(inp_ps=gs_ps_ps_adv_end_houses[1]),
                                             PlayerState(inp_ps=gs_ps_ps_adv_end_houses[2])),
                         [Counter({1: 6}), True])

    def test_get_claimed_plans(self):
        self.assertEqual(get_claimed_plans(GameState(gs_ps_ps_adv_end_houses[0]),
                                           PlayerState(inp_ps=gs_ps_ps_adv_end_houses[1]),
                                           PlayerState(inp_ps=gs_ps_ps_adv_end_houses[2])),
                         [Counter(), ['end houses']])
        self.assertEqual(get_claimed_plans(GameState(gs_ps_ps_invalid[0]),
                                           PlayerState(inp_ps=gs_ps_ps_invalid[1]),
                                           PlayerState(inp_ps=gs_ps_ps_invalid[2])),
                         [Counter(), []])

    def test_check_advanced_plans(self):
        self.assertRaises(InvalidMove, lambda: check_advanced_plans("7 temps",
                                                                    PlayerState(inp_ps=gs_ps_ps_adv_end_houses[1]),
                                                                    PlayerState(inp_ps=gs_ps_ps_adv_end_houses[2])))
        self.assertEqual(check_advanced_plans("end houses",
                                               PlayerState(inp_ps=gs_ps_ps_adv_end_houses[1]),
                                               PlayerState(inp_ps=gs_ps_ps_adv_end_houses[2])),
                          None)
