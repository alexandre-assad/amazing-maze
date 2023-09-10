import random
from Materials.Labyrinth import Labyrinth
from Utils.os_utils import *
from Utils.txt_utils import *

def backtrackGenerator(len,file):
    Lab1 = Labyrinth(len)
    Lab1.board[0][0].visited = True
    # Tant que toute les cases n'ont pas été découvertes
    #Je m'avance vers une case adjaçante si possible
    #Si toute les cases autours ont été vu, je reviens en arrière
    #Si compteur arrive à la fin, je return lab
    case_arround = Lab1.case_unvisited_arround(0,0)
    random.shuffle(case_arround)
    compteur = 1
    Lab1.wall_break(getDirection(0,0,case_arround[0][0],case_arround[0][1]),0,0)
    Lab1 = backtrackAlgo(Lab1,case_arround[0][0],case_arround[0][1],compteur=compteur)
    write_txt(Lab1.display(),file)


def backtrackAlgo(laby,x,y,compteur):
    laby.board[x][y].visited = True
    compteur +=1
    if compteur == laby.length**2:
        return laby
    elif laby.case_unvisited_arround(x,y) == []:
        return laby
    else:
        while True:
            if laby.case_unvisited_arround(x,y) != []:
                case_arround = laby.case_unvisited_arround(x,y)
                random.shuffle(case_arround)
                laby.wall_break(getDirection(x,y,case_arround[0][0],case_arround[0][1]),x,y)
                laby = backtrackAlgo(laby,case_arround[0][0],case_arround[0][1],compteur=compteur)
            else:
                return laby

def getDirection(x1:int,y1:int,x2:int,y2:int) -> str:
    if x1 > x2 and y1 == y2:
        return "Top"
    elif x1 < x2 and y1 == y2:
        return "Bottom"
    elif x1 == x2 and y1 > y2:
        return "Left"
    else:
        return "Right"
