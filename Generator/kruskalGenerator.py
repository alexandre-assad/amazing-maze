import random
import math
from Materials.Labyrinth import Labyrinth
from Utils.os_utils import *
from Utils.txt_utils import *

def kruskalGenerator(len,file):
    Lab1 = Labyrinth(len)
    Lab1.board[0][0].visited = True
    case_arround = Lab1.case_number_arround(0,0)
    random.shuffle(case_arround)
    compteur = 1
    Lab1.board[0][0].k_number,Lab1.board[case_arround[0][0]][case_arround[0][1]].k_number = min(Lab1.board[0][0].k_number,Lab1.board[case_arround[0][0]][case_arround[0][1]].k_number),min(Lab1.board[0][0].k_number,Lab1.board[case_arround[0][0]][case_arround[0][1]].k_number)
    Lab1.wall_break(getDirection(0,0,case_arround[0][0],case_arround[0][1]),0,0)
    Lab1 = backtrackAlgo(Lab1,case_arround[0][0],case_arround[0][1],compteur=compteur)
    write_txt(Lab1.display(),file)
    return Lab1

def backtrackAlgo(laby,x,y,compteur):
    if laby.board[x][y].k_number == 0:
        compteur +=1
    if compteur == laby.length**2:
        return laby
    elif laby.case_number_arround(x,y) == []:
        random_case = getRandomCase(laby)
        return backtrackAlgo(laby,random_case[0],random_case[1],compteur)
    else:
        while True:
            if laby.case_number_arround(x,y) != []:
                case_arround = laby.case_number_arround(x,y)
                random.shuffle(case_arround)
                if laby.board[x][y].k_number < laby.board[case_arround[0][0]][case_arround[0][1]].k_number:
                    laby.board[x][y].k_number,laby.board[case_arround[0][0]][case_arround[0][1]].k_number = min(laby.board[x][y].k_number,laby.board[case_arround[0][0]][case_arround[0][1]].k_number),min(laby.board[x][y].k_number,laby.board[case_arround[0][0]][case_arround[0][1]].k_number)
                    laby.wall_break(getDirection(x,y,case_arround[0][0],case_arround[0][1]),x,y)
                    return backtrackAlgo(laby,case_arround[0][0],case_arround[0][1],compteur=compteur)
                else:
                    laby.board[x][y].k_number,laby.board[case_arround[0][0]][case_arround[0][1]].k_number = min(laby.board[x][y].k_number,laby.board[case_arround[0][0]][case_arround[0][1]].k_number),min(laby.board[x][y].k_number,laby.board[case_arround[0][0]][case_arround[0][1]].k_number)
                    laby.wall_break(getDirection(x,y,case_arround[0][0],case_arround[0][1]),x,y)
                    return backtrackAlgo(laby,x,y,compteur=compteur)
            else:
                random_case = getRandomCase(laby)
                return backtrackAlgo(laby,random_case[0],random_case[1],compteur)

def getDirection(x1:int,y1:int,x2:int,y2:int) -> str:
    if x1 > x2 and y1 == y2:
        return "Top"
    elif x1 < x2 and y1 == y2:
        return "Bottom"
    elif x1 == x2 and y1 > y2:
        return "Left"
    else:
        return "Right"

def getRandomCase(laby):
    while True:
        x, y = random.randint(0,laby.length-1),random.randint(0,laby.length-1)
        if laby.case_number_arround(x,y) != []:
            return [x,y]