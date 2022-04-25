from unittest import TestCase
from my_python.a3_1.Street import *
from contracts import ContractNotRespected


valid_num_houses1 = {
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
}
valid_num_houses2 = {
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
invalid_num_houses1 = {
    "homes": ["blank", False,
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False]],
    "parks": 0,
    "pools": [False, False, False]
}
invalid_num_houses2 = {
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
          [False, "blank", False],
          [False, "blank", False]],
    "parks": 0,
    "pools": [False, False, False]
}
valid_parks1 = {
    "homes": ["blank", False,
          [False, 1, False],
          [False, "blank", False],
          [False, 2, False],
          [False, 3, False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False]],
    "parks": 3,
    "pools": [False, False, False]
}
valid_parks2 = {
    "homes": ["blank", False,
          [False, 1, False],
          [False, 2, False],
          [False, 3, False],
          [False, 4, False],
          [False, [4, "bis"], False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False]],
    "parks": 4,
    "pools": [False, False, False]
}
valid_parks3 = {
    "homes": ["blank", False,
          [False, 3, False],
          [False, 4, False],
          [False, "blank", False],
          [False, "blank", False],
          [False, 6, False],
          [False, 7, False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, 10, False],
          [False, 11, False]],
    "parks": 5,
    "pools": [False, False, False]
}

valid_parks4 = {
    "homes": ["blank", False,
          [False, 3, False],
          [False, 4, False],
          [False, "blank", False],
          [False, "blank", False],
          [False, 6, False],
          [False, 7, False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, 10, False],
          [False, 11, False]],
    "parks": 2,
    "pools": [False, False, False]
}
invalid_parks1 = {
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
    "parks": 4,
    "pools": [False, False, False]
}
invalid_parks2 = {
    "homes": ["blank", False,
          [False, 3, False],
          [False, [3, "bis"], False],
          [False, [3, "bis"], False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False]],
    "parks": 3,
    "pools": [False, False, False]
}
pool_0_1_valid = {
    "homes": ["blank", False,
          [False, "blank", False],
          [False, 1, False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False]],
    "parks": 0,
    "pools": [True, False, False]
}
pool_0_1_invalid = {
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
    "pools": [True, False, False]
}
pool_0_1_invalid_bis = {
    "homes": ["blank", False,
          [False, "blank", False],
          [False, [1, "bis"], False],
          [False, 1, False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False]],
    "parks": 0,
    "pools": [True, False, False]
}
pool_2_2_valid = {
    "homes": ["blank", False,
              [False, "blank", False],
              [False, [1, "bis"], False],
              [False, 1, False],
              [False, "blank", False],
              [False, "blank", False],
              [False, 2, False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False]],
    "parks": 0,
    "pools": [False, True, False]
}
pool_2_2_invalid = {
    "homes": ["blank", False,
              [False, "blank", False],
              [False, [1, "bis"], False],
              [False, 1, False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False]],
    "parks": 0,
    "pools": [False, True, False]
}
pool_1_3_valid = {
    "homes": [1, False,
              [False, "blank", False],
              [False, "blank", False],
              [False, 2, False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, 3, False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False]],
    "parks": 0,
    "pools": [True, True, True]
}
pool_1_3_invalid = {
    "homes": ["blank", False,
              [False, 1, False],
              [False, 2, False],
              [False, "blank", False],
              [False, 3, False],
              [False, 4, False],
              [False, 5, False],
              [False, "blank", False],
              [False, 6, False],
              [False, 7, False],
              [False, 8, False]],
    "parks": 0,
    "pools": [True, True, True]
}

class TestStreet(TestCase):
    # {"homes": homes, "parks": natural, "pools": [bool, bool, bool]}

    def test_get_street_num(self):
        self.assertTrue(Street(valid_num_houses1).get_street_num() == 0)
        self.assertTrue(Street(valid_num_houses2).get_street_num() == 2)
        self.assertRaises(ContractNotRespected, lambda: Street(invalid_num_houses1).get_street_num())
        self.assertRaises(ContractNotRespected, lambda: Street(invalid_num_houses2).get_street_num())

    def test_contracts(self):
        ### Test validation for num of houses on the street ###
        self.assertEqual(Street(valid_num_houses1).homes.get_num_houses(), 10)
        self.assertEqual(Street(valid_num_houses2).homes.get_num_houses(), 12)
        self.assertRaises(ContractNotRespected, lambda: Street(invalid_num_houses1).homes.get_num_houses())
        self.assertRaises(ContractNotRespected, lambda: Street(invalid_num_houses2).homes.get_num_houses())

        # ----- Testing validation for pools ------
        self.assertTrue(Street(pool_0_1_valid))
        self.assertTrue(Street(pool_1_3_valid))
        self.assertTrue(Street(pool_2_2_valid))
        self.assertRaises(AssertionError, lambda: Street(pool_0_1_invalid))
        self.assertRaises(AssertionError, lambda: Street(pool_0_1_invalid_bis))
        self.assertRaises(AssertionError, lambda: Street(pool_2_2_invalid))
        self.assertRaises(AssertionError, lambda: Street(pool_1_3_invalid))

    def test_get_parks(self):
        self.fail()

    def test_get_pools(self):
        self.fail()
