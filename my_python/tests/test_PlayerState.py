import sys
sys.path.append('../../')
from my_python.PlayerState import PlayerState
from my_python.exceptions import InvalidPlayerState
from my_python.tests.input_test_PlayerState import *
from unittest import TestCase



class TestPlayerState(TestCase):
    def test_constructor(self):
        self.assertTrue(PlayerState(inp_ps=empty_valid))
        self.assertRaises(InvalidPlayerState, lambda: PlayerState(inp_ps=street_lens_invalid))

        # NOTE: didn't account for having a claimed score but no built homes in our validators
        # self.assertRaises(InvalidPlayerState, lambda: PlayerState(inp_ps=city_plan_invalid_score_built_homes))
        self.assertRaises(InvalidPlayerState, lambda: PlayerState(inp_ps=agents_invalid_len))
        self.assertRaises(InvalidPlayerState, lambda: PlayerState(inp_ps=agents_invalid_vals))
        self.assertRaises(InvalidPlayerState, lambda: PlayerState(inp_ps=refusals_invalid_neg1))
        self.assertRaises(InvalidPlayerState, lambda: PlayerState(inp_ps=refusals_invalid_four))
        self.assertRaises(InvalidPlayerState, lambda: PlayerState(inp_ps=temps_too_small))
        self.assertRaises(InvalidPlayerState, lambda: PlayerState(inp_ps=temps_too_large))
        self.assertRaises(InvalidPlayerState, lambda: PlayerState(inp_ps=agents_invalid_ind0))
        self.assertRaises(InvalidPlayerState, lambda: PlayerState(inp_ps=agents_invalid_ind4))
        self.assertRaises(InvalidPlayerState, lambda: PlayerState(inp_ps=city_plan_invalid_geq_zero))

        # NOTE: didn't account for built fence but no built homes (same as below)
        # self.assertRaises(InvalidPlayerState, lambda: PlayerState(inp_ps=get_total_built_fences_invalid1))
        # NOTE: didn't account for number of effects played being checked against number of built homes
        # self.assertRaises(InvalidPlayerState, lambda: PlayerState(inp_ps=misc_sum_invalid))
        self.assertTrue(PlayerState(inp_ps=misc_sum_valid))

        # NOTE: didn't account for built fence but no built homes
        # self.assertRaises(InvalidPlayerState, lambda: PlayerState(inp_ps=misc_sum_invalid_fences))

    def test_sub(self):
        self.assertEqual(PlayerState(inp_ps=empty_valid) - PlayerState(inp_ps=empty_valid),
                         PlayerState(agents=all_same_ps["agents"],
                                     city_plan_score=all_same_ps["city-plan-score"],
                                     refusals=all_same_ps["refusals"],
                                     streets=all_same_ps["streets"],
                                     temps=all_same_ps["temps"]))
        self.assertEqual(PlayerState(inp_ps=invalid_misc_sum) - PlayerState(inp_ps=empty_valid),
                         PlayerState(agents=get_total_built_fences_valid2_empty_valid_sub_ps["agents"],
                                     city_plan_score=get_total_built_fences_valid2_empty_valid_sub_ps["city-plan-score"],
                                     refusals=get_total_built_fences_valid2_empty_valid_sub_ps["refusals"],
                                     streets=get_total_built_fences_valid2_empty_valid_sub_ps["streets"],
                                     temps=get_total_built_fences_valid2_empty_valid_sub_ps["temps"]))
