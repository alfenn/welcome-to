import sys

sys.path.append('../../../../')
from my_python.Street import Street
from my_python.Same import Same
from my_python.exceptions import InvalidPlayerState
from unittest import TestCase


class TestStreet(TestCase):
    def test_constructor(self):
        self.assertRaises(InvalidPlayerState, lambda: Street(inp_street=invalid_num_houses1))
        self.assertRaises(InvalidPlayerState, lambda: Street(inp_street=invalid_num_houses2))
        # ----- Testing validation for pools ------
        self.assertTrue(Street(inp_street=pool_0_1_valid))
        self.assertTrue(Street(inp_street=pool_1_3_valid))
        self.assertTrue(Street(inp_street=pool_2_2_valid))
        self.assertRaises(InvalidPlayerState, lambda: Street(inp_street=pool_0_1_invalid))
        self.assertRaises(InvalidPlayerState, lambda: Street(inp_street=pool_0_1_invalid_bis))
        self.assertRaises(InvalidPlayerState, lambda: Street(inp_street=pool_2_2_invalid))
        self.assertRaises(InvalidPlayerState, lambda: Street(inp_street=pool_1_3_invalid))

    def test_get_fields(self):
        # Houses
        self.assertEqual(len(Street(inp_street=valid_num_houses1).houses), 10)
        self.assertEqual(len(Street(inp_street=valid_num_houses2).houses), 12)
        # Parks
        self.assertEqual(Street(inp_street=valid_num_houses1).parks, 0)
        self.assertEqual(Street(inp_street=valid_num_houses2).parks, 0)
        self.assertEqual(Street(inp_street=valid_parks1).parks, 3)
        self.assertEqual(Street(inp_street=valid_parks2).parks, 4)
        self.assertEqual(Street(inp_street=valid_parks3).parks, 5)
        self.assertEqual(Street(inp_street=valid_parks4).parks, 2)
        self.assertRaises(InvalidPlayerState, lambda: Street(inp_street=invalid_parks1).parks)
        self.assertRaises(InvalidPlayerState, lambda: Street(inp_street=invalid_parks2).parks)
        self.assertRaises(InvalidPlayerState, lambda: Street(inp_street=invalid_parks3).parks)

    def test_sub(self):
        self.assertEqual(Street(inp_street=valid_num_houses1) - Street(inp_street=valid_num_houses1),
                         Street(houses=all_same_street_len10["houses"], parks=all_same_street_len10["parks"], pools=all_same_street_len10["pools"]))
        temp_diff = Street(houses=all_same_street_len10["houses"], parks=all_same_street_len10["parks"], pools=all_same_street_len10["pools"])
        temp_diff.houses[1] = House(is_bis=Same(), num=1, is_built=True, used_in_plan=Same(), l_fence=Same(), r_fence=Same())
        temp_diff.houses[2] = House(is_bis=True, num=1, is_built=True, used_in_plan=Same(), l_fence=Same(), r_fence=Same())
        temp_diff.parks = 1
        self.assertEqual(Street(inp_street=valid_num_houses1_2) - Street(inp_street=valid_num_houses1),
                         temp_diff)
