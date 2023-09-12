import sys

from src.Materials.Labyrinth import Labyrinth

from src.Resolver.aStarResolver import aStarResolver
from src.Resolver.backtrackResolver import backtrackResolver

from src.Generator.backtrackGenerator import backtrackGenerator
from src.Generator.kruskalGenerator import kruskalGenerator

from src.Utils.os_utils import *
from src.Utils.txt_utils import *


def main():
    while True:
        try:
            choix = int(input(""" Que voulez vous faire :
    (1) Labyrinthe backtrack, résolution backtrack
    (2) Labyrinthe backtrack, résolution aStar
    (3) Labyrinthe kruskal, résolution backtrack
    (4) Labyrinthe kruskal, résolution aStar
    """))
        except:
            print("Choix invalide")
        if choix not in [1,2,3,4]:
            print("Choix invalide")
        else:
            folder_name = str(input("Comment voulez vous appeler le fichier de génération"))
            os.mkdir(path_folder(folder_name))
            if choix == 1:
                pass


if __name__ == "__main__":
    main()