from search import *
class Board:
    def __init__(self, tiles, width, height,parent = None, length=0, blank  = 0,moves = 0):
        self.tiles = tiles
        self.moves = moves
        self.width = width
        self.height = height
        self.blank = blank
        self.parent = parent
        self.length = length
        self.goal = dict(zip([i for i in range(self.width * self.height)],
                    [(i, j) for i in range(self.height) for j in range(self.width)]))
    def set_parent (self , par):
        self.parent = par
        return
    def find_blank(self):
        """
        this function find the place of the blank tile
        """
        for i in range(self.width):
            for j in range(self.height):
                if self.tiles[i][j] == self.blank:
                    return (i, j)
        return NULL
    def get_legel_moves(self):
        """
        return list of the legel moves that can the bank move to it.
        """
        blank_x,blank_y = self.find_blank()
        moves = []
        if (blank_x > 0):
            moves.append((blank_x-1, blank_y))
        if (blank_x < self.width - 1):
            moves.append((blank_x+1, blank_y))
        if (blank_y > 0):
            moves.append((blank_x, blank_y-1))
        if (blank_y < self.height - 1):
            moves.append((blank_x, blank_y+1))
        return moves
    def move(self, p1 , p2):
        """
        swap the values of p1 and p2 together.
        """
        p1_x , p1_y = p1
        p2_x , p2_y = p2
        temp = self.tiles[p1_x][p1_y]
        self.tiles[p1_x][p1_y] = self.tiles[p2_x][p2_y]
        self.tiles[p2_x][p2_y] = temp
        self.moves += 1
        return
    def goal_test(self):
        """
        check  if the current state is the goal state or nt.
        """
        cnt = self.blank
        for i in range(self.width):
            for j in range(self.height):
                if self.tiles[i][j] != cnt:
                    return False
                cnt += 1
        return True
    def goal_postion(self, value):
        """
        take value and return the postion that it should be in to reach the
        goal sata eg: 8 return (2, 2)
        """
        return self.goal[value]
