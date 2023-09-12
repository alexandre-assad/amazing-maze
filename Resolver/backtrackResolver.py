import random
from Materials.Labyrinth import Labyrinth
from Utils.txt_utils import *



def backtrackGenerator(len,file):
    Lab1 = Labyrinth(len)
    Lab1.board[0][0].visited = True
    # Tant que toute les cases n'ont pas été découvertes
    #Je m'avance vers une case adjaçante si possible
    #Si toute les cases autours ont été vu, je reviens en arrière
    #Si compteur arrive à la fin, je return lab
    case_arround = Lab1.case_wallopen_arround(0,0)
    random.shuffle(case_arround)
    Lab1 = backtrackAlgo(Lab1,case_arround[0][0],case_arround[0][1])
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