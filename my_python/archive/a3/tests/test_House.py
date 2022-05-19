from unittest import TestCase
from contracts import ContractNotRespected
from my_python.archive.a3.House import House

class TestHouse(TestCase):
    def test_contracts(self):
        self.assertRaises(ContractNotRespected, lambda: House("truck"))
        self.assertRaises(ContractNotRespected, lambda: House([]))
        self.assertRaises(ContractNotRespected, lambda: House([1, 2, 3]))
        self.assertRaises(ContractNotRespected, lambda: House(-1))
        self.assertRaises(AssertionError, lambda: House(18))
        self.assertRaises(ContractNotRespected, lambda: House([0, "truck"]))

    def test_is_built(self):
        self.assertTrue(House([0, "bis"]).is_built())
        self.assertTrue(House([17, "bis"]).is_built())
        self.assertTrue(House(0).is_built())
        self.assertTrue(House(17).is_built())
        self.assertFalse(House("blank").is_built())

    def test_is_bis(self):
        self.assertTrue(House([0, "bis"]).get_is_bis())
        self.assertTrue(House([17, "bis"]).get_is_bis())
        self.assertFalse(House(0).get_is_bis())
        self.assertFalse(House(17).get_is_bis())

    def test_get_num(self):
        self.assertEqual(House([0, "bis"]).get_num(), 0)
        self.assertEqual(House([17, "bis"]).get_num(), 17)
        self.assertEqual(House(0).get_num(), 0)
        self.assertEqual(House("blank").get_num(), -1)
