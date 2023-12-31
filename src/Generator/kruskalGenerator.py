import random
from src.Materials.Labyrinth import Labyrinth
from src.Utils.os_utils import *
from src.Utils.txt_utils import *


def kruskalGenerator(length: int, file: str, folder: str) -> Labyrinth:
    """
    This function takes a length and a file name and generates a labyrinth
    using a kruskal algorithm
    """
    Lab1 = Labyrinth(length)
    case_around = Lab1.case_number_around(0, 0)
    random.shuffle(case_around)
    propagation(Lab1, [0, 0], case_around[0])

    while len(Lab1.kruskal_cell["0"]) < Lab1.length**2:
        x, y = random.randint(0, Lab1.length - 1), random.randint(0, Lab1.length - 1)
        case_around = Lab1.case_number_around(x, y)

        if case_around != []:
            random.shuffle(case_around)
            propagation(Lab1, [x, y], case_around[0])

    write_txt(Lab1.display(), file, folder)

    return Lab1


def propagation(laby: Labyrinth, pos1: list, pos2: list) -> None:
    """
    This function takes a labyrinth and two positions and propagates the number
    """
    laby.wall_break(getDirection(pos1[0], pos1[1], pos2[0], pos2[1]), pos1[0], pos1[1])

    number = min(
        laby.board[pos1[0]][pos1[1]].k_number, laby.board[pos2[0]][pos2[1]].k_number
    )
    other_number = max(
        laby.board[pos1[0]][pos1[1]].k_number, laby.board[pos2[0]][pos2[1]].k_number
    )

    for pos_propaged in laby.kruskal_cell[str(other_number)]:
        laby.board[pos_propaged[0]][pos_propaged[1]].k_number = number

        laby.kruskal_cell[str(number)].append([pos_propaged[0], pos_propaged[1]])

    laby.kruskal_cell[str(other_number)] = []

    return None


def getDirection(x1: int, y1: int, x2: int, y2: int) -> str:
    """
    This function takes two positions and returns the direction between them
    """
    if x1 > x2 and y1 == y2:
        return "Top"
    elif x1 < x2 and y1 == y2:
        return "Bottom"
    elif x1 == x2 and y1 > y2:
        return "Left"
    else:
        return "Right"
