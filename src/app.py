from src.layout.events import *


def main() -> None:
    
    running, isSolved = True, False
    mazeMenuIndex, methodMenuIndex, mazeSize= 0, 0, 50
    
    while running:
        
        drawScreen()
        selectMazeGenerator(mazeMenuIndex)
        selectMethodMenu(methodMenuIndex)
        selectIsSolved(isSolved)
        selectMazeSize(mazeSize)
        
        events = pygame.event.get()

        for event in events:
            
            generateMaze(event, mazeMenuIndex, methodMenuIndex, mazeSize)
            
            mazeSize = plusminusMazeSize(event, mazeSize)
            
            isSolved = triggerSolved(event, isSolved)
            
            running = ESC_KEYDOWN(event)

            methodMenuIndex = UP_DOWN_keys(event, methodMenuIndex)
            
            mazeMenuIndex= LEFT_RIGHT_keys(event, mazeMenuIndex)
            
        pygame.display.update()
        
    return None