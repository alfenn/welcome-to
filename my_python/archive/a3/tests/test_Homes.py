from unittest import TestCase
from contracts import ContractNotRespected
from my_python.archive.a3.Homes import Homes
from my_python.archive.a3.HomesElem import HomesElem

class TestHomes(TestCase):
    assertionerror1 = ["blank", True,
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False],
                       [False, "blank", False]]
    invalid1 = ["blank", "true",
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False]]
    invalid2 = [25, True,
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False]]
    invalid3 = ["blank"]
    invalid4 = [[False, "blank", False],
                {},
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False]]
    invalid5 = ["blank", False,
                [True, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False]]
    invalid6 = [1, False,
                [False, 1, False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False],
                [False, "blank", False]]
    valid1 = ["blank", False,
              [True, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False]]
    valid2 = [2, True,
              [True, 3, True],
              [True, 5, False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, 10, False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False],
              [False, "blank", False]]

    valid_bis1 = [2, True,
                  [True, 3, True],
                  [True, 5, False],
                  [False, "blank", False],
                  [False, "blank", False],
                  [False, [10, "bis"], False],
                  [False, 10, False],
                  [False, "blank", False],
                  [False, [12, "bis"], True],
                  [False, 12, True],
                  [False, "blank", False],
                  [False, "blank", False]]

    valid_bis2 = [2, True,
                  [True, 3, True],
                  [True, 5, False],
                  [False, "blank", False],
                  [False, "blank", False],
                  [False, "blank", False],
                  [False, 10, False],
                  [False, [10, "bis"], False],
                  [False, "blank", False],
                  [False, "blank", False],
                  [False, "blank", False],
                  [False, "blank", False]]

    valid_bis3 = [[3, "bis"], True,
                  [True, 3, True],
                  [True, 5, False],
                  [False, "blank", False],
                  [False, "blank", False],
                  [False, "blank", False],
                  [False, 10, False],
                  [False, "blank", False],
                  [False, "blank", False],
                  [False, "blank", False],
                  [False, "blank", False],
                  [False, "blank", False]]

    valid_bis4 = [2, True,
                  [True, 3, True],
                  [True, 5, False],
                  [False, "blank", False],
                  [False, "blank", False],
                  [False, "blank", False],
                  [False, 10, False],
                  [False, "blank", False],
                  [False, "blank", False],
                  [False, "blank", False],
                  [False, 13, False],
                  [False, [13, "bis"], False]]

    invalid_bis1 = [3, True,
                    [True, 3, True],
                    [True, 5, False],
                    [False, "blank", False],
                    [False, "blank", False],
                    [False, "blank", False],
                    [False, 10, False],
                    [False, "blank", False],
                    [False, "blank", False],
                    [False, [10, "bis"], False],
                    [False, "blank", False],
                    [False, "blank", False]]

    invalid_bis2 = [[3, "bis"], True,
                    [True, 3, True],
                    [True, 5, False],
                    [False, "blank", False],
                    [False, "blank", False],
                    [False, "blank", False],
                    [False, 10, False],
                    [False, "blank", False],
                    [False, "blank", False],
                    [False, [10, "bis"], False],
                    [False, "blank", False],
                    [False, "blank", False]]

    invalid_bis3 = [[3, "bis"], True,
                    [True, [3, "bis"], True],
                    [True, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False]]

    invalid_bis4 = [2, True,
                    [True, [3, "bis"], True],
                    [True, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False]]

    invalid_bis5 = ["blank", False,
                    [True, 2, True],
                    [True, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, [3, "bis"], False]]

    invalid_bis6 = ["blank", False,
                    [True, 2, True],
                    [True, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, 4, False],
                    [False, 5, False],
                    [False, [5, "bis"], False],
                    [False, 6, False],
                    [False, 7, False],
                    [False, 8, False],
                    [False, 9, False],
                    [False, 10, False]]

    invalid_bis7 = ["blank", False,
                    [True, 3, True],
                    [True, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, 4, False],
                    [False, [4, "bis"], False],
                    [False, [5, "bis"], False],
                    [False, [5, "bis"], False],
                    [False, [5, "bis"], False],
                    [False, 8, False],
                    [False, 9, False],
                    [False, 10, False]]

    invalid_ascending1 = [10, False,
                          [False, 1, False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False]]

    invalid_ascending2 = [10, False,
                          [False, 1, False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, "blank", False],
                          [False, 3, False],
                          [False, 4, False],
                          [False, 5, False],
                          [False, 6, False]]

    invalid_dup1 = ["blank", False,
                    [True, 3, True],
                    [True, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, 4, False],
                    [False, 4, False],
                    [False, [5, "bis"], False],
                    [False, [5, "bis"], False],
                    [False, [5, "bis"], False],
                    [False, 8, False],
                    [False, 9, False],
                    [False, 10, False]]

    invalid_dup2 = ["blank", False,
                    [True, 3, True],
                    [True, [3, "bis"], False],
                    [False, [3, "bis"], False],
                    [False, 4, False],
                    [False, "blank", False],
                    [False, [5, "bis"], False],
                    [False, [5, "bis"], False],
                    [False, [5, "bis"], False],
                    [False, 8, False],
                    [False, 10, False],
                    [False, 10, False]]

    fence_btwn_bis_valid1 = [2, True,
                  [True, 3, True],
                  [True, 5, False],
                  [False, "blank", False],
                  [False, "blank", False],
                  [False, "blank", False],
                  [True, 10, False],
                  [False, [10, "bis"], False],
                  [True, "blank", False],
                  [False, "blank", False],
                  [True, 13, False],
                  [False, [13, "bis"], False]]

    fence_btwn_bis_invalid1 = ["blank", False,
                             [True, 3, True],
                             [True, [3, "bis"], False],
                             [True, [3, "bis"], False],
                             [False, 4, False],
                             [False, "blank", False],
                             [False, [5, "bis"], False],
                             [False, [5, "bis"], False],
                             [False, [5, "bis"], False],
                             [False, 8, False],
                             [False, 10, False],
                             [False, 10, False]]

    def test_contracts(self):
        self.assertRaises(AssertionError, lambda: Homes(self.assertionerror1))
        self.assertRaises(ContractNotRespected, lambda: Homes(self.invalid1))
        self.assertRaises(AssertionError, lambda: Homes(self.invalid2))
        self.assertRaises(ContractNotRespected, lambda: Homes(self.invalid3))
        self.assertRaises(ContractNotRespected, lambda: Homes(self.invalid4))
        self.assertRaises(ContractNotRespected, lambda: Homes(self.invalid5))
        self.assertTrue(Homes(self.valid1))
        self.assertTrue(Homes(self.valid2))

    def test_get(self):
        homes1 = Homes(self.valid1)
        homes2 = Homes(self.valid2)
        self.assertEqual(homes1.get(0), HomesElem("blank", False))
        self.assertEqual(homes1.get(9), HomesElem("blank", False))
        self.assertRaises(AssertionError, lambda: homes1.get(-1))
        self.assertRaises(AssertionError, lambda: homes1.get(10))
        self.assertEqual(homes2.get(0), HomesElem(2, True))
        self.assertEqual(homes2.get(2), HomesElem(5, False))
        self.assertEqual(homes2.get(6), HomesElem(10, False))
        self.assertEqual(homes2.get(11), HomesElem("blank", False))

    def test_get_num_houses(self):
        homes1 = Homes(self.valid1)
        homes2 = Homes(self.valid2)
        self.assertEqual(homes1.get_num_houses(), 10)
        self.assertEqual(homes1.get(homes1.get_num_houses() - 1), HomesElem("blank", False))
        self.assertEqual(homes2.get_num_houses(), 12)
        self.assertEqual(homes2.get(homes2.get_num_houses() - 1), HomesElem("blank", False))

    def test_validate_bis(self):
        homes1 = Homes(self.valid1)
        homes2 = Homes(self.valid2)
        homes_vbis1 = Homes(self.valid_bis1)
        homes_vbis2 = Homes(self.valid_bis2)
        homes_vbis3 = Homes(self.valid_bis3)
        homes_vbis4 = Homes(self.valid_bis4)
        homes_ibis1 = Homes(self.invalid_bis1)
        homes_ibis2 = Homes(self.invalid_bis2)
        homes_ibis3 = Homes(self.invalid_bis3)
        homes_ibis4 = Homes(self.invalid_bis4)
        homes_ibis5 = Homes(self.invalid_bis5)
        homes_ibis6 = Homes(self.invalid_bis6)
        homes_ibis7 = Homes(self.invalid_bis7)
        self.assertTrue(homes1.validate_bis())
        self.assertTrue(homes2.validate_bis())
        self.assertTrue(homes_vbis1.validate_bis())
        self.assertTrue(homes_vbis2.validate_bis())
        self.assertTrue(homes_vbis3.validate_bis())
        self.assertTrue(homes_vbis4.validate_bis())
        self.assertRaises(AssertionError, lambda: homes_ibis1.validate_bis())
        self.assertRaises(AssertionError, lambda: homes_ibis2.validate_bis())
        self.assertRaises(AssertionError, lambda: homes_ibis3.validate_bis())
        self.assertRaises(AssertionError, lambda: homes_ibis4.validate_bis())
        self.assertRaises(AssertionError, lambda: homes_ibis5.validate_bis())
        self.assertRaises(AssertionError, lambda: homes_ibis6.validate_bis())
        self.assertRaises(AssertionError, lambda: homes_ibis7.validate_bis())

    def test_validate_ascending_order(self):
        homes1 = Homes(self.valid1)
        homes2 = Homes(self.valid2)
        homes_vbis1 = Homes(self.valid_bis1)
        homes_vbis2 = Homes(self.valid_bis2)
        homes_vbis3 = Homes(self.valid_bis3)
        homes_vbis4 = Homes(self.valid_bis4)
        homes_ibis1 = Homes(self.invalid_bis1)
        homes_ibis2 = Homes(self.invalid_bis2)
        homes_ibis3 = Homes(self.invalid_bis3)
        homes_ibis4 = Homes(self.invalid_bis4)
        homes_ibis5 = Homes(self.invalid_bis5)
        homes_ibis6 = Homes(self.invalid_bis6)
        homes_ibis7 = Homes(self.invalid_bis7)
        homes_invalid_ascending1 = Homes(self.invalid_ascending1)
        homes_invalid_ascending2 = Homes(self.invalid_ascending2)
        self.assertTrue(homes1.validate_ascending_order())
        self.assertTrue(homes2.validate_ascending_order())
        self.assertTrue(homes_vbis1.validate_ascending_order())
        self.assertTrue(homes_vbis2.validate_ascending_order())
        self.assertTrue(homes_vbis3.validate_ascending_order())
        self.assertTrue(homes_vbis4.validate_ascending_order())
        self.assertTrue(homes_ibis1.validate_ascending_order())
        self.assertTrue(homes_ibis2.validate_ascending_order())
        self.assertTrue(homes_ibis3.validate_ascending_order())
        self.assertTrue(homes_ibis4.validate_ascending_order())
        self.assertTrue(homes_ibis5.validate_ascending_order())
        self.assertTrue(homes_ibis6.validate_ascending_order())
        self.assertTrue(homes_ibis7.validate_ascending_order())
        self.assertRaises(AssertionError, lambda: homes_invalid_ascending1.validate_ascending_order())
        self.assertRaises(AssertionError, lambda: homes_invalid_ascending2.validate_ascending_order())

    def test_validate_no_dups(self):
        homes1 = Homes(self.valid1)
        homes2 = Homes(self.valid2)
        homes_vbis1 = Homes(self.valid_bis1)
        homes_vbis2 = Homes(self.valid_bis2)
        homes_vbis3 = Homes(self.valid_bis3)
        homes_vbis4 = Homes(self.valid_bis4)
        homes_ibis1 = Homes(self.invalid_bis1)
        homes_ibis2 = Homes(self.invalid_bis2)
        homes_ibis3 = Homes(self.invalid_bis3)
        homes_ibis4 = Homes(self.invalid_bis4)
        homes_ibis5 = Homes(self.invalid_bis5)
        homes_ibis6 = Homes(self.invalid_bis6)
        homes_ibis7 = Homes(self.invalid_bis7)
        homes_invalid_ascending1 = Homes(self.invalid_ascending1)
        homes_invalid_ascending2 = Homes(self.invalid_ascending2)
        homes_invalid_dup1 = Homes(self.invalid_dup1)
        homes_invalid_dup2 = Homes(self.invalid_dup2)
        self.assertTrue(homes1.validate_no_dups())
        self.assertTrue(homes2.validate_no_dups())
        self.assertTrue(homes_vbis1.validate_no_dups())
        self.assertTrue(homes_vbis2.validate_no_dups())
        self.assertTrue(homes_vbis3.validate_no_dups())
        self.assertTrue(homes_vbis4.validate_no_dups())
        self.assertRaises(AssertionError, lambda: homes_ibis1.validate_no_dups())
        self.assertTrue(homes_ibis2.validate_no_dups())
        self.assertTrue(homes_ibis3.validate_no_dups())
        self.assertTrue(homes_ibis4.validate_no_dups())
        self.assertTrue(homes_ibis5.validate_no_dups())
        self.assertTrue(homes_ibis6.validate_no_dups())
        self.assertTrue(homes_ibis7.validate_no_dups())
        self.assertTrue(homes_invalid_ascending1.validate_no_dups())
        self.assertTrue(homes_invalid_ascending2.validate_no_dups())
        self.assertRaises(AssertionError, lambda: homes_invalid_dup1.validate_no_dups())
        self.assertRaises(AssertionError, lambda:homes_invalid_dup2.validate_no_dups())

    def test_validate_no_fences_between_bis(self):
        val_h1 = Homes(self.fence_btwn_bis_valid1)
        inv_h1 = Homes(self.fence_btwn_bis_invalid1)
        self.assertTrue(val_h1.validate_no_fences_between_bis())
        self.assertRaises(AssertionError, lambda: inv_h1.validate_no_fences_between_bis())

    def test_get_num_built_fences(self):
        val_h1 = Homes(self.fence_btwn_bis_valid1)
        inv_h1 = Homes(self.fence_btwn_bis_invalid1)
        self.assertEqual(val_h1.get_num_built_fences(), 7)
        self.assertEqual(inv_h1.get_num_built_fences(), 5)