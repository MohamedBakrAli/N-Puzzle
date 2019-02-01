import queue
from board import *
from copy import deepcopy
import math



def bfs(board):
    Q = []
    Q.append(board)
    vis=[]
    intial_state=board.tiles
    goal_state = None
    while Q:
        temp_list = Q.pop(0)
        vis.append(temp_list.tiles)
        if temp_list.goal_test():
            goal_state = temp_list
            print('bfs finish')
            break
        else :

            for move in temp_list.get_legel_moves():
                temp_board = deepcopy(temp_list)
                temp_board.move(temp_list.find_blank() , move)

                if (temp_board.tiles not in vis) and find_2(Q,temp_board)==-1:
                    #print(temp_board.tiles)
                    temp_board.set_parent(temp_list)
                    Q.append(temp_board)
                    #vis.append(temp_board.tiles)

            #print(len(Q))
    answer = []
    while goal_state.parent != None:
        answer.append(goal_state.tiles)
        goal_state = goal_state.parent

    return answer

def find_2(list_of_board, board):
    """
    return -1 if board not exist in the list
    """
    t=[]
    for i in range(len(list_of_board)):
        t.append(list_of_board[i].tiles)

    if  board.tiles not in t:
        return -1
    return 1

def dfs(board,max_length = 100):
    explored = []
    frontiers = [board]
    goal_state = None
    depth=0
    while frontiers:
    	state = frontiers.pop()
    	explored.append(state)
    	if(state.length>depth):
    	    depth = state.length
    	if state.goal_test():
    	    print ("DFS Path found")
    	    goal_state = state
    	    break
    	else :
    	    if state.length==max_length:
    	        explored.remove(state)
    	        continue

    	neighbors = get_neighbors(state)
    	for neighbor in neighbors:
            if not found(neighbor,explored,frontiers):
                neighbor.set_parent(state)
                frontiers.append(neighbor)
    if goal_state == None:
        return [], depth
    answer = []
    while goal_state.parent != None:
        answer.append(goal_state.tiles)
        goal_state = goal_state.parent

    return answer, depth

def found(state,explored,frontiers):
    for x in explored:
        if(state.tiles == x.tiles):
            return True
    for x in frontiers:
        if(state.tiles == x.tiles):
            return True
    return False
def get_neighbors(state):
    neighbors = list()
    moves = state.get_legel_moves()
    for move in moves:
        new_state = deepcopy(state)
        new_state.length = state.length+1
        new_state.move(state.find_blank(),move)
        neighbors.append(new_state)
    return neighbors

def A_star(board, h_fn):
    if board.goal_test():
        return [board.tiles]
    frontier = []
    frontier.append((-1, board))
    explored = []
    goal_state = None
    x = 0
    while frontier:
        (cost, state, i) = min_board(frontier)
        frontier.pop(i)
        if state.tiles not in explored:
            explored.append(state.tiles)
        if (state.goal_test()):
            print("A* finish")
            goal_state = state
            break
        for move in state.get_legel_moves():
            copy_board = deepcopy(state)
            copy_board.move(copy_board.find_blank(), move)
            copy_board.set_parent(state)
            # the index of copy_board in the frontier list
            copy_index = find(frontier, copy_board)
            # f(n) = h(n) + g(n) where g(n) is fixed for all possible move from current board
            # calculate the cost of this move acording to the given h_fun
            new_cost = h_fn(copy_board) + copy_board.moves
            if (copy_board.tiles not in explored) and copy_index == -1:
                frontier.append((new_cost, copy_board))
            # it will never enter in this condation in this problem as the h fn
            # is depend in the board not in the path to this board.
            elif copy_index != -1:
                old_cost, b = frontier[copy_index]
                if (old_cost < new_cost):
                    b.set_parent(state)
                    frontier[copy_index] = (new_cost,b)
    answer = []
    while goal_state.parent != None:
        answer.append(goal_state.tiles)
        goal_state = goal_state.parent

    return answer


def find(list_of_board, board):
    """
    return index  if the board is in the list_of_board and -1 else
    """
    for i in range(len(list_of_board)):
        cost, b = list_of_board[i]
        if b.tiles == board.tiles:
            return i
    return -1

def min_board(list_of_board):
    """
    get the board with the min cost
    """
    cost = float("inf")
    board = None
    index = -1
    for i in range(len(list_of_board)):
        elem_cost, elem_board = list_of_board[i]
        if (elem_cost < cost):
            cost = elem_cost
            board = elem_board
            index = i
    return (cost,board,index)

def h_manhattan(board):
    """
    Manhattan Distance It is the sum of absolute values of differences
    in the goals x and y coordinates and the current cells x andy coordinates
    respectively.
    """
    h = 0
    for i in range(board.width):
        for j in range(board.height):
            if (board.tiles[i][j]):
                (goal_x, goal_y) = board.goal_postion(board.tiles[i][j])
                h += abs(i - goal_x) + abs(j - goal_y)
    return h

def h_euclidean(board):
    """
    Euclidean Distance It is the distance between the current cell and the
    goal cell using the distance formula
    """
    h = 0
    for i in range(board.width):
        for j in range(board.height):
            if (board.tiles[i][j]):
                (goal_x, goal_y) = board.goal_postion(board.tiles[i][j])
                h +=  math.sqrt(((i - goal_x) ** 2) + ((j - goal_y) ** 2))
    return h
