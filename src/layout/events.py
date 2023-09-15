from src.layout.display import *

def UP_DOWN_keys(event: pygame.event,default_menu_index: int) -> tuple[int, bool]:
    """
    This function is responsible for changing the default_menu_index.
    It takes as input the event and the solved boolean. It returns the
     default_menu_index and the solved boolean.
    """

    if K_UP_func(event):
        default_menu_index = (default_menu_index - 1) % 2
    if K_DOWN_func(event):
        default_menu_index = (default_menu_index + 1) % 2

    return default_menu_index


def LEFT_RIGHT_keys(
    event: pygame.event, default_menu_index: int
) -> tuple[int, bool]:
    """
    This function is responsible for changing the other_menu_index.
     It takes as input the event, the other_menu_index, and the solved boolean.
     It returns the other_menu_index and the solved boolean.
    """

    if K_LEFT_func(event):
        default_menu_index = (default_menu_index - 1) % 2
    if K_RIGHT_func(event):
        default_menu_index = (default_menu_index + 1) % 2

    return default_menu_index

def generateMaze(event: pygame.event, generationIndex: int, solvingIndex: int, mazeSize: int) -> None:
    """
    Displays the maze as a PNG image
    """
    generationArray = [backtrackGenerator, kruskalGenerator]
    solvingArray = [aStarResolver, backtrackResolver]
    
    if RETURN_KEYDOWN(event):
        generationArray[generationIndex](mazeSize,"generated.txt","temp")
        ascii2PNG(False,path_txt("temp","generated.txt"),path_txt("temp","generated_ascii.png"))
        write_txt(solvingArray[solvingIndex]("temp","generated.txt").displayResolver(),"resolver.txt","temp")
        ascii2PNG(True,path_txt("temp","resolver.txt"),path_txt("temp","resolver_ascii.png"))

    return None

def plusminusMazeSize(event: pygame.event, mazeSize: int) -> int:
    """
    Displays the maze as a PNG image
    """
    if P_KEYDOWN(event):
        mazeSize += 1
    if M_KEYDOWN(event):
        mazeSize -= 1
    return mazeSize
    

def triggerSolved(event: pygame.event, isSolved: bool) -> bool:
    """
    Displays the maze as a PNG image
    """
    if S_KEYDOWN(event):
        isSolved = not isSolved
    return isSolved
    