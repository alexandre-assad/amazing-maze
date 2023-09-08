from Materials.Case import Case


class Labyrinth:

    def __init__(self,length):
        self.length = length
        self.board = self.setup()


    def setup(self):
        board = []
        sub_board = []
        for li in range(self.length):
            for col in range(self.length):
                sub_board.append(Case(li,col))
            board.append(sub_board)
            sub_board = []
        return board