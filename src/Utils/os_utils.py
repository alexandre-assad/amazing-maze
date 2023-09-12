import os


def path_txt(folder,file):
    txt_path = path_folder(folder)
    return os.path.join(txt_path,file)


 

def path_folder(directory):
    return os.path.join("Labyrinth_files",directory)