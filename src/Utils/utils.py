from src.Materials.Labyrinth import *
from src.Materials.Case import *
from src.Utils.txt_utils import *

"""
What is utils?
"""

def txt_to_labyrinth(file:str) -> Labyrinth:
    
    str_labyrinth = read_txt(file)
    i=0
    
    while str_labyrinth[i] != "#":
        
        str_labyrinth = str_labyrinth[1:]
        i+=1
    length = 0
    while True:
        if str_labyrinth[length] != "\n":
            length +=1
        else:
            break

    lab1 = Labyrinth(int((length)/2))

    list_lab = list(str_labyrinth)
    
    new_list = []
    sub_list = []
    
    for i in range(len(list_lab)):
        if list_lab[i] != '\n':
            sub_list.append(list_lab[i])
        else:
            new_list.append(sub_list)
            sub_list = []
    new_list.append(["#"for i in range(length)])

    for i in range(1,2*lab1.length,2):
        
        for j in range(1,2*lab1.length,2):
            
            if new_list[i-1][j] == " ":
                lab1.board[int((i-1)/2)][int((j-1)/2)].walls["Top"] = False
            if new_list[i+1][j] == " ":
                lab1.board[int((i-1)/2)][int((j-1)/2)].walls["Bottom"] = False
            if new_list[i][j-1] == " ":
                lab1.board[int((i-1)/2)][int((j-1)/2)].walls["Left"] = False
            if new_list[i][j+1] == " ":
                lab1.board[int((i-1)/2)][int((j-1)/2)].walls["Right"] = False

    return lab1