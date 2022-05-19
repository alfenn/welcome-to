from unittest import TestCase
from my_python.archive.a3.Street import *
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
num_estates_0_valid = {
    "homes": ["blank", False,
          [False, "blank", False],
          [True, 1, False],
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
num_estates_0_1_valid = {
    "homes": ["blank", False,
          [False, "blank", False],
          [True, 1, False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, 2, True]],
    "parks": 0,
    "pools": [False, False, False]
}
num_estates_1_valid = {
    "homes": ["blank", False,
          [False, "blank", False],
          [True, 1, False],
          [False, "blank", False],
          [False, 2, False],
          [True, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [True, 3, False]],
    "parks": 0,
    "pools": [False, False, False]
}
num_estates_2_valid = {
    "homes": ["blank", False,
          [False, "blank", False],
          [True, 1, False],
          [False, 2, False],
          [False, 3, False],
          [True, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [True, 4, False]],
    "parks": 0,
    "pools": [False, False, False]
}
num_estates_3_valid = {
    "homes": ["blank", False,
          [False, "blank", False],
          [True, 1, False],
          [True, 2, False],
          [False, 3, False],
          [True, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [False, "blank", False],
          [True, 4, False]],
    "parks": 0,
    "pools": [False, False, False]
}
num_estates_46_valid = {
    "homes": [1, False,
          [False, 2, False],
          [False, 3, False],
          [False, 4, False],
          [True, 5, False],
          [False, 6, False],
          [False, 7, False],
          [False, 8, False],
          [False, 9, False],
          [False, 10, False]],
    "parks": 0,
    "pools": [False, False, False]
}
num_estates_0_2_valid = {
    "homes": [1, False,
          [False, 2, False],
          [False, 3, False],
          [False, 4, False],
          [False, 5, False],
          [False, 6, False],
          [False, 7, False],
          [False, 8, False],
          [False, 9, False],
          [False, 10, False]],
    "parks": 0,
    "pools": [False, False, False]
}


class TestStreet(TestCase):
    # {"homes": homes, "parks": natural, "pools": [bool, bool, bool]}

    def test_get_street_num(self):
        self.assertTrue(Street(valid_num_houses1).get_street_num() == 0)
        self.assertTrue(Street(valid_num_houses2).get_street_num() == 2)
        self.assertRaises(ContractNotRespected, lambda: Street(invalid_num_houses1).get_street_num())
        self.assertRaises(ContractNotRespected, lambda: Street(invalid_num_houses2).get_street_num())

    def test_contracts(self):
        ### Test validation for num of homes on the street ###
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
        self.assertEqual(Street(valid_num_houses1).get_parks(), 0)
        self.assertEqual(Street(valid_num_houses2).get_parks(), 0)
        self.assertEqual(Street(valid_parks1).get_parks(), 3)
        self.assertEqual(Street(valid_parks2).get_parks(), 4)
        self.assertEqual(Street(valid_parks3).get_parks(), 5)
        self.assertEqual(Street(valid_parks4).get_parks(), 2)
        self.assertRaises(AssertionError, lambda: Street(invalid_parks1).get_parks())
        self.assertRaises(AssertionError, lambda: Street(invalid_parks2).get_parks())

    def test_get_num_bis(self):
        self.assertEqual(Street(valid_num_houses1).get_num_bis(), 0)
        self.assertEqual(Street(pool_2_2_valid).get_num_bis(), 1)

    def test_get_num_estates(self):
        self.assertEqual(Street(num_estates_0_valid).get_num_estates(), [None, 0,0,0,0,0,0])
        self.assertEqual(Street(num_estates_0_1_valid).get_num_estates(), [None, 0, 0, 0, 0, 0, 0])
        self.assertEqual(Street(num_estates_1_valid).get_num_estates(), [None, 1, 0, 0, 0, 0, 0])
        self.assertEqual(Street(num_estates_2_valid).get_num_estates(), [None, 1, 0, 1, 0, 0, 0])
        self.assertEqual(Street(num_estates_3_valid).get_num_estates(), [None, 2, 1, 0, 0, 0, 0])
        self.assertEqual(Street(num_estates_46_valid).get_num_estates(), [None, 0, 0, 0, 1, 0, 1])
        self.assertEqual(Street(num_estates_0_2_valid).get_num_estates(), [None, 0, 0, 0, 0, 0, 0])

    # def test_get_pools(self):
    #     self.assertEqual()


