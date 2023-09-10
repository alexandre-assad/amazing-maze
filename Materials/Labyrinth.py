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
        distanceDisplay= {"Top":[x-1,y],"Bottom":[x+1,y],"Left":[x,y-1],"Right":[x,y+1]}
        opposite_direction = {"Top":"Bottom","Bottom":"Top","Left":"Right","Right":"Left"}

        try:
            self.board[x][y].walls[direction], self.board[distanceDisplay[direction][0]][distanceDisplay[direction][1]].walls[opposite_direction[direction]] = False, False
        except:
            pass
    
    def display(self) -> str:
        """
        Input : self
        Output : a string, the display of the labyrinth 
        """
        display_str = ""
        display_array = []
        line = []
        for i in range(2*self.length+1):
            for j in range(2*self.length+1):
                line.append("#")
            display_array.append(line)
            line = []
        
        #Display array is like [['#','#','#'],[...]...]

       
        perm = "test"
        for li in range(self.length):
            for col in range(self.length):

                display_array[li*2+1][col*2+1] = "."
                if perm == "test":
                    distanceDisplay={"Top":[[li*2,col*2],[li*2,col*2+1],[li*2,col*2+2]],"Bottom":[[li*2+2,col*2],[li*2+2,col*2+1],[li*2+2,col*2+2]],"Left":[[li*2,col*2],[li*2+1,col*2],[li*2+2,col*2]],"Right":[[li*2,col*2+2],[li*2+1,col*2+2],[li*2+2,col*2+2]]}
                    for key,value in self.board[li][col].walls.items():
                        if value == True:
                            display_array[distanceDisplay[key][0][0]][distanceDisplay[key][0][1]], display_array[distanceDisplay[key][1][0]][distanceDisplay[key][1][1]],display_array[distanceDisplay[key][2][0]][distanceDisplay[key][2][1]] = "#","#","#"
                        else:
                            display_array[distanceDisplay[key][1][0]][distanceDisplay[key][1][1]] = " "
                    perm = "untest"
                else:
                    perm = "test"
        
        display_array[0][1],display_array[2*(self.length-1)+1][2*(self.length-1)+2] = " ", " "

        for ligne in display_array:
            for char in ligne:
                display_str += char
            display_str += "\n"
        return "\n"+display_str[:len(display_str)-1]
    

    def case_unvisited_arround(self,x:int,y:int) ->list:
        case_arround = []
        try:
            if self.board[x-1][y].visited == False and x-1 >=0:
                case_arround.append([x-1,y])
        except:
            pass
        try:
            if self.board[x+1][y].visited == False and x+1 <self.length:
                case_arround.append([x+1,y])
        except:
            pass
        try:
            if self.board[x][y-1].visited == False and y-1 >=0:
                case_arround.append([x,y-1])
        except:
            pass
        try:
            if self.board[x][y+1].visited == False and y+1 <self.length:
                case_arround.append([x,y+1])
        except:
            pass
        return case_arround