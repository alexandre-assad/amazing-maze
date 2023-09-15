from src.layout.keydowns import *
from src.layout.colors import Colors
from src.ASCII2JPG.utils.txtExtract import parseTxt
from src.Materials.Labyrinth import Labyrinth
from src.Resolver.aStarResolver import aStarResolver
from src.Resolver.backtrackResolver import backtrackResolver
from src.Generator.backtrackGenerator import backtrackGenerator
from src.Generator.kruskalGenerator import kruskalGenerator
from src.ASCII2JPG.ascii2PNG import ascii2PNG, generateAsciiImage
from src.Utils.os_utils import *
from src.Utils.txt_utils import *
import numpy as np
import os

pygame.init()
pygame.font.init()

mazeSize = 9
increment = 10

SCREEN = pygame.display.set_mode((980, 660))
RECTANGLE = pygame.Surface((900, 580))
GAMEDISPLAY = pygame.Surface((860, 540))
DEFAULTMARGIN = 60
FARMARGIN = 550


def initFont(font_size: int) -> pygame.font.Font:
    """
    Returns a font object with the given font size.
    """
    return pygame.font.Font(
        os.path.join("assets", "fonts", "Retro_Gaming.ttf"), font_size
    )


def drawScreen() -> None:
    """
    Generates a PNG image from a grid and displays it.
    """
    SCREEN.fill(Colors.SILVER)
    SCREEN.blit(RECTANGLE, (40, 70))
    SCREEN.blit(GAMEDISPLAY, (DEFAULTMARGIN, 100))
    GAMEDISPLAY.fill(Colors.BLACK)
    SCREEN.blit(initFont(40).render("Maze Solver", True, Colors.BLACK), (300, increment))
    
    return None


def selectMethodMenu(menu_selection_index: int) -> None:
    """
    Displays the menu to select the method to solve the grid.
    """
    options = [("Backtrack", DEFAULTMARGIN), ("A*", DEFAULTMARGIN)]
    passive_color = Colors.MATRIX
    active_color = Colors.GREEN
    GAMEDISPLAY.blit(
        initFont(25).render("Select Generator: ", True, Colors.MATRIX), (FARMARGIN, increment)
    )
    arrow = "-> "
    for i, (text, y_pos) in enumerate(options):
        y = 50 + y_pos * i
        if i == menu_selection_index:
            text = arrow + text
            blit_color = active_color
        else:
            blit_color = passive_color
        GAMEDISPLAY.blit(initFont(25).render(text, True, blit_color), (FARMARGIN, y))
    
    return None


def selectMazeGenerator(menu_selection_index: int) -> None:
    """
    Displays the menu to select the grid to solve.
    """
    options = [("Backtrack", DEFAULTMARGIN), ("Kruskal", DEFAULTMARGIN)]

    GAMEDISPLAY.blit(
        initFont(25).render("Select Solver: ", True, Colors.MATRIX), (FARMARGIN, 150)
    )
    GAMEDISPLAY.blit(
        initFont(25).render(f"< {options[menu_selection_index][0]} >", True, Colors.GREEN),
        (FARMARGIN, 180),
    )

    return None

def selectIsSolved(isSolved: bool) -> None:
    """
    Displays the menu to select the grid to solve.
    """
    options = [("Solved", Colors.GREEN), ("Unsolved", Colors.RED)]

    GAMEDISPLAY.blit(
        initFont(25).render("Select Solved: ", True, Colors.MATRIX), (FARMARGIN, 250)
    )
    if isSolved:
        GAMEDISPLAY.blit(
            initFont(25).render(f'Press S: {options[0][0]}', True, options[0][1]),
            (FARMARGIN, 280),
        )
    else:
        GAMEDISPLAY.blit(
            initFont(25).render(f'Press S: {options[1][0]}', True, options[1][1]),
            (FARMARGIN, 280),
        )

    return None

def selectMazeSize(sizeIndex: int) -> None:
    """
    Displays the menu to select the grid to solve.
    """

    GAMEDISPLAY.blit(
        initFont(25).render("Select Maze Size:", True, Colors.MATRIX), (FARMARGIN, 350)
    )
    GAMEDISPLAY.blit(
        initFont(25).render(f'(P/M): {sizeIndex}', True, Colors.GREEN), (FARMARGIN, 380)
    )
    return None

def displayMaze(sizeIndex: int, generationIndex: int, solvingIndex: int):
    """
    Displays the maze as a PNG image
    """
    