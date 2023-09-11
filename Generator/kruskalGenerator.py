import random
from Materials.Labyrinth import Labyrinth
from Utils.os_utils import *
from Utils.txt_utils import *

def kruskalGenerator(len,file):
    Lab1 = Labyrinth(len)
    Lab1.board[0][0].visited = True