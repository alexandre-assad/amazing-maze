import sys

from src.Materials.Labyrinth import Labyrinth

from src.Resolver.aStarResolver import aStarResolver
from src.Resolver.backtrackResolver import backtrackResolver

from src.Generator.backtrackGenerator import backtrackGenerator
from src.Generator.kruskalGenerator import kruskalGenerator

from src.ASCII2JPG.ascii2PNG import ascii2PNG

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
            try:
                length = int(input("Veuillez choisir la taille du labyrinthe \n"))
            except:
                length = 10
                print("Taille invalide, voici une simulation sur un labyrinthe 10x10")
            if choix == 1:
                backtrackGenerator(length,"backtrack_generated.txt",folder_name)
                ascii2PNG(False,path_txt(folder_name,"backtrack_generated.txt"),path_txt(folder_name,"backtrack_generated_ascii.png"))
                write_txt(backtrackResolver(folder_name,"backtrack_generated.txt").displayResolver(),"backtrack_resolver.txt",folder_name)
                ascii2PNG(True,path_txt(folder_name,"backtrack_resolver.txt"),path_txt(folder_name,"backtrack_resolver_ascii.png"))
            elif choix == 2:
                backtrackGenerator(length,"backtrack_generated.txt",folder_name)
                ascii2PNG(False,path_txt(folder_name,"backtrack_generated.txt"),path_txt(folder_name,"backtrack_generated_ascii.png"))
                write_txt(aStarResolver(folder_name,"backtrack_generated.txt").displayResolver(),"aStar_resolver.txt",folder_name)
                ascii2PNG(True,path_txt(folder_name,"aStar_resolver.txt"),path_txt(folder_name,"aStar_resolver_ascii.png"))
            elif choix == 3:
                kruskalGenerator(length,"kruskam_generated.txt",folder_name)
                ascii2PNG(False,path_txt(folder_name,"kruskal_generated.txt"),path_txt(folder_name,"kruskal_generated_ascii.png"))
                write_txt(backtrackResolver(folder_name,"kruskal_generated.txt").displayResolver(),"backtrack_resolver.txt",folder_name)
                ascii2PNG(True,path_txt(folder_name,"backtrack_resolver.txt"),path_txt(folder_name,"backtrack_resolver_ascii.png"))
            else:
                kruskalGenerator(length,"kruskal_generated.txt",folder_name)
                ascii2PNG(False,path_txt(folder_name,"kruskal_generated.txt"),path_txt(folder_name,"kruskal_generated_ascii.png"))
                write_txt(aStarResolver(folder_name,"kruskal_generated.txt").displayResolver(),"aStar_resolver.txt",folder_name)
                ascii2PNG(True,path_txt(folder_name,"aStar_resolver.txt"),path_txt(folder_name,"aStar_resolver_ascii.png"))

if __name__ == "__main__":
    main()