# test suite resource: https://docs.python.org/3/library/unittest.html
import unittest

from test_House import TestHouse
from test_Street import TestStreet
from test_PlayerState import TestPlayerState
from test_validate_move import TestValidateMove

if __name__ == '__main__':
    unittest.main(verbosity=2)
