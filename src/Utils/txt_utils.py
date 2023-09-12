from src.Utils.os_utils import *

def read_txt(path:str):
    f = open(path_txt(path),'r')
    return f.read()
    
def write_txt(content:str,file:str,folder:str):
    with open(path_txt(folder,file), 'w') as f:
        f.write(content)