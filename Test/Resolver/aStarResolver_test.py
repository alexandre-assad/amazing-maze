import unittest
from Materials.Labyrinth import Labyrinth
from Generator.kruskalGenerator import *
from Resolver.aStarResolver import *
from Utils.utils import *
from Utils.txt_utils import *

class TestAStarResolver(unittest.TestCase):

    def test_aStarResolver(self):
        Lab1 = aStarResolver("lab5.txt")
        self.assertEqual(Lab1.displayResolver(),"""
#o#####
#o o o#
# # # #
#*#*#o#
# ### #
#* *#oo
#######""")
        write_txt(Lab1.displayResolver(),"lab5_resolver.txt")
        kruskalGenerator(10,"lab6.txt")
        write_txt(aStarResolver("lab6.txt").displayResolver(),"lab6_resolver.txt")