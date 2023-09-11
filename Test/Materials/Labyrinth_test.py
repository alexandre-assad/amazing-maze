import unittest 
from Materials.Labyrinth import Labyrinth


class TestLabyrinth(unittest.TestCase):

    def test_setup(self):
        Lab1 = Labyrinth(9)
        self.assertEqual(Lab1.board[0][0].visited,False)
        self.assertEqual([Lab1.board[2][3].x,Lab1.board[2][3].y],[2,3])
        self.assertEqual(Lab1.board[4][7].walls["Top"],True)
        self.assertEqual(Lab1.board[1][3].k_number,12)


    def test_wall_break(self):
        Lab1 = Labyrinth(3)
        Lab1.wall_break("Right",0,0)
        self.assertEqual([Lab1.board[0][0].walls["Right"],Lab1.board[0][1].walls["Left"]],[False,False])
        self.assertEqual(Lab1.board[0][1].walls["Right"],True)



    def test_case_unvisited_arround(self):
        Lab1 = Labyrinth(3)
        Lab1.board[0][1].visited = True
        self.assertEqual(Lab1.case_unvisited_arround(0,0),[[1,0]])
        self.assertEqual(Lab1.case_unvisited_arround(1,1),[[2,1],[1,0],[1,2]])


    def test_display(self):
        Lab1 = Labyrinth(3)
        Lab1.wall_break("Right",0,0)
        Lab1.wall_break("Bottom",0,1)
        Lab1.wall_break("Right",1,1)
        Lab1.wall_break("Top",1,2)
        Lab1.wall_break("Bottom",1,2)
        Lab1.wall_break("Left",2,2)
        Lab1.wall_break("Left",2,1)
        Lab1.wall_break("Top",2,0)
        self.assertEqual(Lab1.display(),"""
# #####
#. .#.#
### # #
#.#. .#
# ### #
#. . . 
#######""")

        Lab2 = Labyrinth(2)
        Lab2.wall_break("Right",0,0)
        Lab2.wall_break("Bottom",0,1)
        Lab2.wall_break("Left",1,1)
        self.assertEqual(Lab2.display(),"""
# ###
#. .#
### #
#. . 
#####""")

    def test_case_number_arround(self):
        Lab1 = Labyrinth(3)
        Lab1.board[0][1].k_number = 0
        self.assertEqual(Lab1.case_number_arround(0,0),[[1,0]])
        self.assertEqual(Lab1.case_number_arround(1,1),[[0,1],[2,1],[1,0],[1,2]])