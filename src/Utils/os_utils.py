import os


def path_txt(folder: str, file: str) -> str:
    txt_path = path_folder(folder)
    return os.path.join(txt_path, file)

"""
Using join for Windows/Linux parity is good practice!
"""

def path_folder(directory: str) -> str:
    return os.path.join("Labyrinth_files", directory)
