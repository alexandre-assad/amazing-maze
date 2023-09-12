import random
from Materials.Labyrinth import Labyrinth
from Utils.txt_utils import *
from Utils.utils import *



def backtrackResolver(file):
    Lab1 = txt_to_labyrinth(file)
    Lab1.board[0][0].in_way = True
    # Tant que toute les cases n'ont pas été découvertes
    #Je m'avance vers une case adjaçante si possible
    #Si toute les cases autours ont été vu, je reviens en arrière
    #Si compteur arrive à la fin, je return lab
    case_arround = Lab1.case_wallopen_arround(0,0)
    random.shuffle(case_arround)
    Lab1 = backtrackAlgo(Lab1,case_arround[0][0],case_arround[0][1])
    return Lab1


def backtrackAlgo(laby,x,y):
    laby.board[x][y].in_way = True
    laby.board[x][y].visited = True
    if [x,y] == [laby.length-1,laby.length-1]:
        laby.resolve = True
        return laby
    elif laby.case_way_possible(x,y) == []:
        laby.board[x][y].in_way = False
        return laby
    else:
        while True:
            if laby.case_way_possible(x,y) != []:
                case_arround = laby.case_way_possible(x,y)
                random.shuffle(case_arround)
                laby = backtrackAlgo(laby,case_arround[0][0],case_arround[0][1])
                if laby.resolve:
                    return laby
            else:
                return laby
            

def case_way_possible(laby,x,y):
    case_possible = []
    case_wall = laby.case_wallopen_arround(x,y)
    for case in laby.case_unvisited_arround(x,y):
        if case in case_wall:
            case_possible.append(case)
    return case