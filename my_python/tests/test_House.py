import sys
sys.path.append('../../')
from my_python.House import House
from my_python.exceptions import InvalidPlayerState
from my_python.Fence import Fence
from my_python.Same import Same

from unittest import TestCase


class TestHouse(TestCase):
    def test_constructor(self):
        self.assertRaises(InvalidPlayerState, lambda: House(inp_house="truck", used_in_plan=True, l_fence=Fence(True), r_fence=(True)))
        self.assertRaises(InvalidPlayerState, lambda: House(inp_house=[], used_in_plan=True, l_fence=Fence(False), r_fence=Fence(False)))
        self.assertRaises(InvalidPlayerState, lambda: House(inp_house=[1, 2, 3], used_in_plan=False, l_fence=Fence(True), r_fence=Fence(False)))
        self.assertRaises(InvalidPlayerState, lambda: House(inp_house=-1, used_in_plan=True, l_fence=Fence(False), r_fence=Fence(False)))
        self.assertRaises(InvalidPlayerState, lambda: House(inp_house=18, used_in_plan=False, l_fence=Fence(False), r_fence=Fence(False)))
        self.assertRaises(InvalidPlayerState, lambda: House(inp_house=[0, "truck"], used_in_plan=True, l_fence=Fence(False), r_fence=Fence(False)))
        self.assertRaises(InvalidPlayerState, lambda: House(inp_house=["", "truck"], used_in_plan=True, l_fence=Fence(False), r_fence=Fence(False)))

    def test_load(self):
        self.assertEqual(House(inp_house=[0, "bis"], used_in_plan=True, l_fence=Fence(False), r_fence=Fence(False)).load(), [0, "bis"])
        self.assertEqual(House(inp_house=[17, "bis"], used_in_plan=True, l_fence=Fence(False), r_fence=Fence(False)).load(), [17, "bis"])
        self.assertEqual(House(inp_house=0, used_in_plan=True, l_fence=Fence(False), r_fence=Fence(False)).load(), 0)
        self.assertTrue(House(inp_house=17, used_in_plan=True, l_fence=Fence(False), r_fence=Fence(False)).load(), 17)
        self.assertEqual(House(inp_house="blank", used_in_plan=True, l_fence=Fence(False), r_fence=Fence(False)).load(), "blank")

    def test_sub(self):
        self.assertEqual(House(inp_house=[0, "bis"], used_in_plan=True, l_fence=Fence(False), r_fence=Fence(False))
                         - House(inp_house=[0, "bis"], used_in_plan=True, l_fence=Fence(False), r_fence=Fence(False)),
                         House(is_bis=Same(), num=Same(), is_built=Same(), used_in_plan=Same(), l_fence=Same(), r_fence=Same()))
        self.assertEqual(House(inp_house=[0, "bis"], used_in_plan=True, l_fence=Fence(False), r_fence=Fence(False))
                         - House(inp_house=5, used_in_plan=False, l_fence=Fence(False), r_fence=Fence(False)),
                         House(is_bis=True, num=0, used_in_plan=True, l_fence=Same(), r_fence=Same()))