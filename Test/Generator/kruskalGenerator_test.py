import unittest 
from Generator.kruskalGenerator import *
from Utils.txt_utils import *
from Utils.utils import *

class TestKruskalGenerator(unittest.TestCase):

    def test_backtrackGenerator(self):
        Lab2 = kruskalGenerator(3,"kruskal_lab_test.txt")
        self.assertEqual(read_txt("kruskal_lab_test.txt")[0:2],"\n#")
        Lab1 = txt_to_labyrinth("kruskal_lab_test.txt")
        self.assertEqual(Lab1.board[0][0].walls["Top"],True)
        self.assertEqual(Lab1.length,3)
        self.assertEqual(Lab2.board[2][0].k_number, 0)


        