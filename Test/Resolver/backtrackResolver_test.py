import unittest
from Resolver.backtrackResolver import *
from Materials.Labyrinth import Labyrinth
from Utils.utils import *


class TestBacktrackResolver(unittest.TestCase):

    def test_backtrackResolver(self):
        Lab1 = backtrackResolver("lab3.txt")

        self.assertEqual(Lab1.displayResolver(),"""
# #####
#o o o#
# ### #
#*#* o#
# ### #
#* *#o 
#######""")
                         
        write_txt(Lab1.displayResolver(),"lab3.resolver")