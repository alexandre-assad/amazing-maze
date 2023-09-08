import unittest 
from Materials.Labyrinth import Labyrinth


class TestLabyrinth(unittest.TestCase):

    def test_setup(self):
        Lab1 = Labyrinth(9)
        self.assertEqual(Lab1.board[0][0].visited,False)
        self.assertEqual([Lab1.board[2][3].x,Lab1.board[2][3].y],[2,3])
        self.assertEqual(Lab1.board[4][7].walls["Top"],True)


    def test_wall_break(self):
        Lab1 = Labyrinth(3)
        Lab1.wall_break("Right",0,0)
        self.assertEqual([Lab1.board[0][0].walls["Right"],Lab1.board[0][1].walls["Left"]],[False,False])
        self.assertEqual(Lab1.board[0][1].walls["Right"],True)



    def test_display(self):
        Lab1 = Labyrinth(3)
        pass