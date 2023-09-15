from src.Materials.Labyrinth import Labyrinth
from src.Utils.txt_utils import *
from src.Utils.utils import *


def aStarResolver(folder,file: str) -> Labyrinth:
    """
    This is the main function of the aStarResolver
    """
    Lab1 = txt_to_labyrinth(folder,file)
    Lab1.board[0][0].in_way = True
    Lab1 = backtrackAlgo(Lab1, 0, 0)
    return Lab1


def backtrackAlgo(laby: Labyrinth, x: int, y: int) -> Labyrinth:
    """
    This function takes a labyrinth, a position and a counter and generates a labyrinth
    Using a backtracking algorithm
    Inspired by Sebastian Lague video
    """
    open = [] #The set of nodes to be evaluated
    #open will be in the following structure [[node,parent],...]
    closed = [] #The set of nodes arleady evaluated
    #closed will be in the following structure [[node,parent],...]
    open.append(laby.board[x][y]) #Add start to open

    while True: #loop
        open.sort(key=lowestFCost) 
        current = open[0] #current = node in Open with lowest f_cost
        open.remove(current)
        closed.append(current) #add current to closed

        if current.x == laby.length-1 and current.y == laby.length -1:
            #if current is the target node
            return create_path(laby,current)
            #return the path
        
        neighbours = case_way_possible(laby,current.x,current.y)
        #for each neighbour of the current node
        if neighbours != []:
            for neighbour in neighbours:

                neighbour_case = laby.board[neighbour[0]][neighbour[1]]

                #if neighbour is in closed
                if neighbour_case in closed:
                    #pass to the next neighbour
                    continue
                    
                #if new path to neighbour is shorter OR neighbour is not in Open
                if neighbour_case.f_cost < current.f_cost or neighbour_case not in open:
                    #set f_cost of neighbour
                    #set parent of neighbour to current
                    #if neighbour not in open
                    #add neighbour in open
                    laby.board[neighbour[0]][neighbour[1]].parent = current
                    neighbour_case.parent = current

                    laby.board[neighbour[0]][neighbour[1]].f_cost = takeDistanceToEnd(laby,neighbour_case) + takeDistanceToStart(laby,neighbour_case)
                    neighbour_case.f_cost = takeDistanceToEnd(laby,neighbour_case) + takeDistanceToStart(laby,neighbour_case)
                    
                    if neighbour_case not in open:
                        open.append(neighbour_case)
    


def case_way_possible(laby: Labyrinth, x: int, y: int) -> list[list]:
    """
    This function takes a labyrinth and a position and returns the list of the possible way
    """
    case_possible = []
    case_wall = laby.case_wallopen_around(x, y)

    for case in laby.case_unvisited_around(x, y):
        if case in case_wall:
            case_possible.append(case)
    return case_possible


def create_path(laby:Labyrinth,current:Case) -> Labyrinth:
    """
    Input : a Labyrinth and a Case
    Basic code: While exploring case and parenting of case, we mark them in the way in the labyrinth
    Output : The labyrinth modified with the path
    """
    case = current
    while case != laby.board[0][0]:
        laby.board[case.x][case.y].in_way = True
        case = case.parent
    return laby


def takeDistanceToStart(laby:Labyrinth,case:Case) ->int:
    """
    This function takes a labyrinth and a case and returns the distance between the case and the start
    """
    return math.sqrt((case.x-0)**2+(case.y-0)**2)

def takeDistanceToEnd(laby: Labyrinth, case: Case) -> int:
    """
    This function takes a labyrinth and a case and returns the distance between the case and the end
    """
    return laby.board[case.x][case.y].distance_to_end

def lowestFCost(case:Case):
    """
    This function takes a case and returns the f_cost of the case
    """
    return case.f_cost
