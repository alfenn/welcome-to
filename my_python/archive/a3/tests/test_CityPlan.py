from unittest import TestCase
from archive.OldCityPlan import *

spec_valid = {"criteria":[1,1,1,1,1,1],"position":1,"score1":8,"score2":4}
score2_invalid = {"criteria":[1,1,1,1,1,1],"position":1,"score1":8,"score2":True}
score1_invalid = {"criteria":[1,1,1,1,1,1],"position":1,"score1":"hiiiiiii","score2":1}
position_invalid_0 = {"criteria":[1,1,1,1,1,1],"position":0,"score1":8,"score2":4}
position_invalid_str = {"criteria":[1,1,1,1,1,1],"position":"1","score1":8,"score2":4}
position_invalid_bool = {"criteria":[1,1,1,1,1,1],"position":True,"score1":8,"score2":4}
position_invalid_4 = {"criteria":[1,1,1,1,1,1],"position":4,"score1":8,"score2":4}
criteria_invalid_decimal = {"criteria":[0.1,1,1,1,1,1],"position":1,"score1":8,"score2":4}
criteria_invalid_negative = {"criteria":[-1,1,1,1,1,1],"position":1,"score1":8,"score2":4}
criteria_invalid_str1 = {"criteria":["1",1,1,1,1,1],"position":1,"score1":8,"score2":4}
criteria_invalid_str = {"criteria":["hiiiiii",1,1,1,1,1],"position":1,"score1":8,"score2":4}
criteria_invalid_len = {"criteria":[],"position":1,"score1":8,"score2":4}

class TestCityPlan(TestCase):
    def test_contracts(self):
        self.assertTrue(OldCityPlan(spec_valid))
        self.assertRaises(AssertionError, lambda: OldCityPlan(score2_invalid))
        self.assertRaises(AssertionError, lambda: OldCityPlan(score1_invalid))
        self.assertRaises(AssertionError, lambda: OldCityPlan(position_invalid_0))
        self.assertRaises(AssertionError, lambda: OldCityPlan(position_invalid_str))
        self.assertRaises(AssertionError, lambda: OldCityPlan(position_invalid_bool))
        self.assertRaises(AssertionError, lambda: OldCityPlan(position_invalid_4))
        self.assertRaises(AssertionError, lambda: OldCityPlan(criteria_invalid_decimal))
        self.assertRaises(AssertionError, lambda: OldCityPlan(criteria_invalid_negative))
        self.assertRaises(AssertionError, lambda: OldCityPlan(criteria_invalid_str1))
        self.assertRaises(AssertionError, lambda: OldCityPlan(criteria_invalid_str))
        self.assertRaises(AssertionError, lambda: OldCityPlan(criteria_invalid_len))

