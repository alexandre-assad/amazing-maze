from Utils.os_utils import *

def read_txt(path:str):
    f = open(path_txt(path),'r')
    return f.read()
    
def write_txt(content:str,file:str):
    with open(path_txt(file), 'w') as f:
        f.write(content)