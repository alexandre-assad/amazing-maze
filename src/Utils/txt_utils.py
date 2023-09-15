from src.Utils.os_utils import *


def read_txt(folder:str,path: str) -> str:
    """
    This function takes a folder and a file name and returns the content of the file
    """
    f = open(path_txt(folder,path), "r")
    return f.read()


def write_txt(content: str, file: str, folder: str) -> None:
    """
    This function takes a content, a file name and a folder and writes the content in the file
    """
    with open(path_txt(folder, file), "w") as f:
        f.write(content)
    return None
