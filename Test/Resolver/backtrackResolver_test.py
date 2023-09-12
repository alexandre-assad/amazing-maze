import unittest
from Resolver.backtrackResolver import *
from Generator.kruskalGenerator import *
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
        write_txt(Lab1.displayResolver(),"lab3_resolver.txt")
        kruskalGenerator(100,"lab4.txt")
        lab2 = backtrackResolver("lab4.txt")
        write_txt(lab2.displayResolver(),"lab4_resolver.txt")