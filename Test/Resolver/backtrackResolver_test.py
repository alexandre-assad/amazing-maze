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
        lab2 = backtrackResolver("lab4.txt")
        self.assertEqual([lab2.board[1][0].in_way,lab2.board[1][1].in_way],[True,True])
        self.assertEqual(lab2.board[0][1].in_way,False)
        self.assertEqual(lab2.displayResolver(),"""
# #######
#o * * *#
# ### ###
#o o#* *#
### #####
#* o o o#
# ##### #
#* *#* o 
#########
"""[:-1])
        write_txt(lab2.displayResolver(),"lab4_resolver.txt")