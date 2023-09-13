from src.Utils.os_utils import *


def read_txt(folder:str,path: str) -> str:
    f = open(path_txt(folder,path), "r")
    return f.read()


def write_txt(content: str, file: str, folder: str) -> None:
    
    with open(path_txt(folder, file), "w") as f:
        f.write(content)
    return None
