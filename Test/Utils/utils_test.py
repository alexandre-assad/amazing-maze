import unittest
from Materials.Labyrinth import *
from Utils.utils import *

class TestUtils(unittest.TestCase):

    def test_txt_to_labyrinth(self):
        lab1 = txt_to_labyrinth("lab3")
        self.assertEqual(lab1.board[0][0].walls["Right"],False)
        self.assertEqual(lab1.board[0][0].walls["Top"],True)
        self.assertEqual(lab1.length,3)