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