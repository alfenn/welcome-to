from unittest import TestCase
from contracts import ContractNotRespected
from my_python.archive.a3.HomesElem import HomesElem
from my_python.archive.a3.House import House

class TestHomesElem(TestCase):
    def test_contracts(self):
        self.assertRaises(ContractNotRespected, lambda: HomesElem("bogus", True))
        self.assertRaises(ContractNotRespected, lambda: HomesElem(25, False))
        self.assertRaises(ContractNotRespected, lambda: HomesElem("blank", "happy"))
        self.assertRaises(AssertionError, lambda: HomesElem("blank", True))
        self.assertRaises(AssertionError, lambda: HomesElem("blank", True))
        self.assertTrue(HomesElem(17, True))
        self.assertTrue(HomesElem("blank", False))
        self.assertTrue(HomesElem(1, True))

    def test_get_house(self):
        self.assertEqual(HomesElem(2, True).get_house(), House(2))
        self.assertEqual(HomesElem("blank", False).get_house(), House("blank"))
        self.assertEqual(HomesElem("blank", False).get_house(), House("blank"))

    def test_get_used_in_plan(self):
        self.assertEqual(HomesElem(0, True).get_used_in_plan(), True)
        self.assertEqual(HomesElem(17, False).get_used_in_plan(), False)
