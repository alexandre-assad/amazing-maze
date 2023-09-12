import unittest
from Materials.Labyrinth import Labyrinth
from Generator.kruskalGenerator import *
from Resolver.aStarResolver import *
from Utils.utils import *
from Utils.txt_utils import *

class TestAStarResolver(unittest.TestCase):

    def test_aStarResolver(self):
        Lab1 = txt_to_labyrinth("lab5.txt")
        self.assertEqual(Lab1.displayResolver(),"""
# #####
#o o o#
# # # #
#*#*#o#
# ### #
#* *#o 
#######""")