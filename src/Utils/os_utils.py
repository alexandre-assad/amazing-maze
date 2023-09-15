import os

def path_txt(folder: str, file: str) -> str:
    """
    This function takes a folder and a file name and returns the path to the file
    It is used to get the path to the txt files regardless of the OS"""
    txt_path = path_folder(folder)
    return os.path.join(txt_path, file)


def path_folder(directory: str) -> str:
    """
    This function takes a directory and returns the path to the directory
    It is used to get the path to the txt files regardless of the OS and link to the directory"""
    return os.path.join("Labyrinth_files", directory)
