from unittest import TestCase

from contracts import ContractNotRespected

from my_python.a3_1.House import House

class TestHouse(TestCase):
    def test_is_built(self):
        h_built1 = House([0, "bis"])
        h_built2 = House([17, "bis"])
        h_built3 = House(0)
        h_built4 = House(17)
        h_notbuilt1 = House("blank")
        self.assertTrue(h_built1)
        self.assertTrue(h_built2)
        self.assertTrue(h_built3)
        self.assertTrue(h_built4)
        self.assertTrue(h_notbuilt1)
        self.assertRaises(ContractNotRespected, House("truck"))
        self.assertRaises(ContractNotRespected, House([]))
        self.assertRaises(ContractNotRespected, House([1,2,3]))
        self.assertRaises(ContractNotRespected, House(-1))
        self.assertRaises(ContractNotRespected, House(18))
        self.assertRaises(ContractNotRespected, House([0, "truck"]))

    def test_is_bis(self):
        self.fail()

    def test_get_num(self):
        self.fail()
