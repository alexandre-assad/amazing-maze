import unittest
from Generator.kruskalGenerator import *
from Utils.txt_utils import *
from Utils.utils import *


class TestKruskalGenerator(unittest.TestCase):
    def test_backtrackGenerator(self):
        kruskalGenerator(3, "lab3.txt")
        Lab2 = kruskalGenerator(100, "kruskal_lab_test.txt")
        self.assertEqual(read_txt("kruskal_lab_test.txt")[0:2], "\n#")
        Lab1 = txt_to_labyrinth("kruskal_lab_test.txt")
        self.assertEqual(Lab1.board[0][0].walls["Top"], True)
        self.assertEqual(Lab1.length, 100)
        self.assertEqual(Lab2.board[2][5].k_number, 0)
        self.assertEqual(len(Lab2.kruskal_cell["0"]), 100**2)
        self.assertNotEqual(
            Lab2.board[3][4].walls,
            {"Top": True, "Bottom": True, "Left": True, "Right": True},
        )

    def test_propagation(self):
        Lab1 = Labyrinth(3)
        propagation(Lab1, [0, 1], [0, 2])
        self.assertEqual(Lab1.kruskal_cell["1"], [[0, 1], [0, 2]])
        self.assertEqual(Lab1.board[0][1].walls["Right"], False)
        self.assertEqual(Lab1.board[0][2].k_number, 1)
        self.assertEqual(Lab1.kruskal_cell["2"], [])
        propagation(Lab1, [0, 0], [0, 1])
        self.assertEqual(Lab1.board[0][2].k_number, 0)
        self.assertEqual(Lab1.kruskal_cell["0"], [[0, 0], [0, 1], [0, 2]])
        self.assertEqual(Lab1.kruskal_cell["1"], [])
