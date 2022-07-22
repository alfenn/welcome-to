import sys
sys.path.append('../../')
from my_python.House import House
from my_python.exceptions import InvalidPlayerState
from my_python.Fence import Fence
from my_python.Same import Same

from unittest import TestCase


class TestHouse(TestCase):
    def test_constructor_contracts(self):
        self.assertRaises(InvalidPlayerState, lambda: House(inp_house="truck", used_in_plan=True, l_fence=Fence(True), r_fence=(True)))
        self.assertRaises(InvalidPlayerState, lambda: House(inp_house=[], used_in_plan=True, l_fence=Fence(False), r_fence=Fence(False)))
        self.assertRaises(InvalidPlayerState, lambda: House(inp_house=[1, 2, 3], used_in_plan=False, l_fence=Fence(True), r_fence=Fence(False)))
        self.assertRaises(InvalidPlayerState, lambda: House(inp_house=-1, used_in_plan=True, l_fence=Fence(False), r_fence=Fence(False)))
        self.assertRaises(InvalidPlayerState, lambda: House(inp_house=18, used_in_plan=False, l_fence=Fence(False), r_fence=Fence(False)))
        self.assertRaises(InvalidPlayerState, lambda: House(inp_house=[0, "truck"], used_in_plan=True, l_fence=Fence(False), r_fence=Fence(False)))
        self.assertRaises(InvalidPlayerState, lambda: House(inp_house=["", "truck"], used_in_plan=True, l_fence=Fence(False), r_fence=Fence(False)))