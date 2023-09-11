

class Case:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = {"Top":True,"Left":True,"Right":True,"Bottom":True}
        self.k_number = 0
