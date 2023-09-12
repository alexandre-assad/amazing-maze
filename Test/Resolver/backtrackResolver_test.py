import unittest
from Resolver.backtrackResolver import *
from Materials.Labyrinth import Labyrinth
from Utils.utils import *


class TestBacktrackResolver(unittest.TestCase):

    def test_backtrackResolver(self):
        Lab1 = txt_to_labyrinth("lab3")
        self.assertEqual(Lab1.displayResolver(),"""
# #####
#o o#*#
### # #
#*#o o#
# ### #
#* * o
#######""")