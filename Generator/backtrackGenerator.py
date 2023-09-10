import random
from Materials.Labyrinth import Labyrinth
from Utils.os_utils import *
from Utils.txt_utils import *

def backtrackGenerator(len,file):
    Lab1 = Labyrinth(len)
    
    if Lab1.case_unvisited_arround(0,0) == []:
        return
    else:
        pass