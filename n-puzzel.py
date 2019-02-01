import math
import random
import time
from copy import deepcopy
from board import *
from search import *



def get_random_puzzle(n):
    # generate list of random number of the range of 0 to n
    l = random.sample(range(0, n + 1), n + 1)

    while not check_solvable(l, n+ 1):
        l = random.sample(range(0, n + 1), n + 1)
    # convert the list l to 2D list
    w = int(math.sqrt(n + 1))
    return [list(i) for i in zip(*[l[i:i+w] for i in range(0, n+1, w)])]

def check_solvable(l , length):
    inversions = 0
    for i in range(length):
        for j in range(i+1, length):
            if l[i] and l[j] and l[i] > l[j]:
                inversions += 1
    return (inversions % 2) == 0

def print_matrix(tiles, rows, columns):
    # maximum width of column, including spaces
    pad_len = len(str(rows * columns)) + 1

    for i in range(rows):
        for j in range(columns):
            print("\t\t{n:>{pad}}".format(n=tiles[i][j], pad=pad_len), end='')
        print()

def print_moves(answer, w):
    for i in range(len(answer)):
        print ("#Move : ", i, "\n")
        print_matrix(answer[len(answer) - 1 - i], w, w)

if __name__ == '__main__':
    #print(check_solvable([6, 3, 4, 5, 0, 2, 8 , 1, 7], 9))
    print("\t\tWelcom in n-puzzel solver\n")
    n = int(input("Enter N :"))
    width = int(math.sqrt(n + 1))
    while (width * width) != (n + 1):
        n = int (input("Enter invalid N :"))
        width = int(math.sqrt(n + 1))

    # generate random n-puzzel
    tiles = get_random_puzzle(n)
    #tiles = [[1,2,5],[3,4,0],[6,7,8]]
    intial_board = Board(tiles, width,width)
    print ("the intial", n, "puzzel board:")
    print_matrix(tiles, width, width)
    exit = False
    while not exit:
        print ("The Algorithms :")
        print ("1) BFS.")
        print ("2) DFS.")
        print ("3) A* with Manhattan heuristic.")
        print ("4) A* with Euclidean heuristic.")
        print ("5) Exit.")
        c = int(input("Enter the number of Algorithm :"))
        if (c == 1):
            # BFS
            start = time.time()
            answer= bfs(deepcopy(intial_board))
            end =time.time()
            print_moves(answer, width)
            print ("the number of moves : ", len(answer) - 1)
            print ("the search time : ", end - start , "s.\n")
        elif(c == 2):
            # DFS
            start = time.time()
            answer,depth= dfs(deepcopy(intial_board), 20)
            end =time.time()
            if (answer == []):
                print("DFS can not reach a solution")
            else :
                print_moves(answer, width)
                print ("the number of moves : ", len(answer) - 1)

            print("DFS depth search is :", depth)
            print ("the search time : ", end - start , "s.\n")

        elif(c == 3):
            # A* with Manhattan heuristic.
            start = time.time()
            answer= A_star(deepcopy(intial_board), h_manhattan)
            end =time.time()
            print_moves(answer, width)
            print ("the number of moves : ", len(answer) - 1)
            print ("the search time : ", end - start , "s.\n")
        elif(c == 4):
            # A* with  Euclidean heuristic.
            start = time.time()
            answer= A_star(deepcopy(intial_board), h_euclidean)
            end =time.time()
            print_moves(answer, width)
            print ("the number of moves : ", len(answer) - 1)
            print ("the search time : ", end - start , "s.\n")
        elif(c == 5):
            exit = True
        else:
            print ("Invalid input !")

    print ("Godbye 6_6")
