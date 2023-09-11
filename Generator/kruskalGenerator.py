import random
import math
from Materials.Labyrinth import Labyrinth
from Utils.os_utils import *
from Utils.txt_utils import *

def kruskalGenerator(len:int,file:str) -> Labyrinth:
    Lab1 = Labyrinth(len)
    case_arround = Lab1.case_number_arround(0,0)
    random.shuffle(case_arround)
    Lab1 = propagation(Lab1,[0,0],case_arround[0])
    while Lab1.krustal_cell["0"].len < Lab1.length**2:
        x,y = random.randint[0,Lab1.length-1],random.randint[0,Lab1.length-1]
        case_arround = Lab1.case_number_arround(x,y)
        random.shuffle(case_arround)        
        Lab1 = propagation([0,0],case_arround[0])
    write_txt(Lab1.display(),file)
    return Lab1

def propagation(laby:Labyrinth,pos1:list,pos2:list) -> Labyrinth:
    laby.wall_break(getDirection(pos1[0],pos1[1],pos2[0],pos2[1]),pos1[0],pos1[1])
    number = min(laby.board[pos1[0]][pos1[1]].k_number,laby.board[pos2[0]][pos2[1]].k_number)
    other_number = max(laby.board[pos1[0]][pos1[1]].k_number,laby.board[pos2[0]][pos2[1]].k_number)
    for pos_propaged in laby.krustal_cell[str(other_number)]:
        laby.board[pos_propaged[0]][pos_propaged[1]].k_number = number
        laby.krustal_cell[str(number)].append([pos_propaged[0],pos_propaged[1]])
        laby.krustal_cell[str(other_number)].remove([pos_propaged[0],pos_propaged[1]])
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