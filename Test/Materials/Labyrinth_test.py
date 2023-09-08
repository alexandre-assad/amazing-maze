import unittest 
from Materials.Labyrinth import Labyrinth


class TestLabyrinth(unittest.TestCase):

    def test_setup(self):
        Lab1 = Labyrinth(9)
        self.assertEqual(Lab1.board[0][0].visited,False)
        self.assertEqual([Lab1[2][3].x,Lab1[2][3].y],[2,3])
        self.assertEqual(Lab1[4][7].walls["Top"],True)