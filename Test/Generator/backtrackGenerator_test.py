import unittest 
from Generator.backtrackGenerator import *
from Utils.txt_utils import *
from Utils.utils import *

class TestBacktrackGenerator(unittest.TestCase):

    def test_backtrackGenerator(self):
        backtrackGenerator(4,"backtrack_lab_test.txt")
        self.assertEqual(read_txt("backtrack_lab_test.txt")[0:2],"##")
        Lab1 = txt_to_labyrinth("backtrack_lab_test.txt")
        self.assertEqual(Lab1.board[0][0].walls["Top"],True)