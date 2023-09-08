from Materials.Case import Case


class Labyrinth:

    def __init__(self,length):
        self.length = length
        self.board = self.setup()


    def setup(self):
        """
        Input : self
        Output : a double matrix, the board of Cases
        """
        board = []
        sub_board = []
        for li in range(self.length):
            for col in range(self.length):
                sub_board.append(Case(li,col))
            board.append(sub_board)
            sub_board = []
        #The board is closed, so now we can see it as a box of little closed box, to create the labyrinth we'll destroy Case.wall
        return board
    
    def wall_break(self,direction:str,x:int,y:int):
        """
        Input : a direction, and two int coordinate
        Basic code : For the direction, break the wall of the cell at the coordinate, and the opposite wall of the next cell
        Output : self 
        """
        distance = {"Top":[x-1,y],"Bottom":[x+1,y],"Left":[x,y-1],"Right":[x,y+1]}
        opposite_direction = {"Top":"Bottom","Bottom":"Top","Left":"Right","Right":"Left"}
        self.board[x][y].walls[direction], self.board[distance[direction][0]][distance[direction][1]].walls[opposite_direction[direction]] = False, False
