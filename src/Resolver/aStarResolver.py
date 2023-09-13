import random
from src.Materials.Labyrinth import Labyrinth
from src.Utils.txt_utils import *
from src.Utils.utils import *

"""
class AStarResolver:?
"""


def aStarResolver(file: str) -> Labyrinth:
    Lab1 = txt_to_labyrinth(file)
    # Tant que toute les cases n'ont pas été découvertes
    # Je m'avance vers une case adjaçante si possible
    # Si toute les cases autours ont été vu, je reviens en arrière
    # Si compteur arrive à la fin, je return lab

    Lab1 = backtrackAlgo(Lab1, 0, 0)
    return Lab1


def backtrackAlgo(laby: Labyrinth, x: int, y: int) -> Labyrinth:
    laby.board[x][y].in_way = True
    laby.board[x][y].visited = True

    if [x, y] == [laby.length - 1, laby.length - 1]:
        laby.resolve = True
        return laby

    elif case_way_possible(laby, x, y) == []:
        laby.board[x][y].in_way = False
        return laby

    else:
        while True:
            if case_way_possible(laby, x, y) != []:
                case_around = case_way_possible(laby, x, y)
                case_around.sort(key=lambda x: takeDistanceToEnd(laby, x))
                laby = backtrackAlgo(laby, case_around[0][0], case_around[0][1])
                if laby.resolve:
                    return laby
            else:
                laby.board[x][y].in_way = False
                return laby


def case_way_possible(laby: Labyrinth, x: int, y: int) -> list[list]:
    case_possible = []
    case_wall = laby.case_wallopen_around(x, y)

    for case in laby.case_unvisited_around(x, y):
        if case in case_wall:
            case_possible.append(case)
    return case_possible


def takeDistanceToEnd(laby: Labyrinth, case: Case) -> int:
    return laby.board[case[0]][case[1]].distance_to_end
