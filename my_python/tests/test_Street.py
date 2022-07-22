import sys

sys.path.append('../../')
from my_python.Street import Street
from my_python.Same import Same
from my_python.exceptions import InvalidPlayerState
from unittest import TestCase
from my_python.tests.input_test_Street import *


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
        self.assertEqual(len(Street(inp_street=valid_num_houses1).homes), 10)
        self.assertEqual(len(Street(inp_street=valid_num_houses2).homes), 12)
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

    def test_validate_ascending_order(self):
        container["homes"] = valid1
        self.assertTrue(Street(inp_street=container))
        container["homes"] = valid2
        self.assertTrue(Street(inp_street=container))
        container["homes"] = valid_bis1
        self.assertTrue(Street(inp_street=container))
        container["homes"] = valid_bis2
        self.assertTrue(Street(inp_street=container))
        container["homes"] = valid_bis3
        self.assertTrue(Street(inp_street=container))
        container["homes"] = valid_bis4
        self.assertTrue(Street(inp_street=container))
        container["homes"] = invalid_ascending1
        self.assertRaises(InvalidPlayerState, lambda: Street(inp_street=container))
        container["homes"] = invalid_ascending2
        self.assertRaises(InvalidPlayerState, lambda: Street(inp_street=container))

    def test_validate_no_dups(self):
        container["homes"] = valid1
        self.assertTrue(Street(inp_street=container))
        container["homes"] = valid2
        self.assertTrue(Street(inp_street=container))
        container["homes"] = valid_bis1
        self.assertTrue(Street(inp_street=container))
        container["homes"] = valid_bis2
        self.assertTrue(Street(inp_street=container))
        container["homes"] = valid_bis3
        self.assertTrue(Street(inp_street=container))
        container["homes"] = valid_bis4
        self.assertTrue(Street(inp_street=container))
        container["homes"] = invalid_ascending1
        self.assertRaises(InvalidPlayerState, lambda: Street(inp_street=container))
        container["homes"] = invalid_ascending2
        self.assertRaises(InvalidPlayerState, lambda: Street(inp_street=container))
        container["homes"] = invalid_dup1
        self.assertRaises(InvalidPlayerState, lambda: Street(inp_street=container))
        container["homes"] = invalid_dup2
        self.assertRaises(InvalidPlayerState, lambda: Street(inp_street=container))

