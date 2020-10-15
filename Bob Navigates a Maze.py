import math
import os
import random
import re
import sys

# Edit this function
def minMoves(maze, x, y):
    """
    1 <= maze rows and columns <= 100
    0 <= num of coins <= 10
    1 <= x < maze rows
    1 <= y < maze columns
    """

    # helper: returns shortest distance between current block and target
    def helper(maze, visited, coins, i, j, x, y, path):
        print("path= "+str(path))
        print("location ="+str([i,j]))
        print("----------------")
        # if current location is one of these:
        # 1. out of boarder
        # 2. previous location from last recursion
        # 3. empty spot (marked as 1)
        # then it cannot be reached and should return max path length
        if (i < 0 or j < 0 or i >= len(maze) or j >= len(maze[0])) or maze[i][j] == 1 or visited[i][j] == True:
            return 10000

        # if reach target
        if (i == x and j == y) and coins == 0:
            return path

        # recursion
        visited[i][j] = True # mark current location
        if maze[i][j] == 2: coins -= 1
        print("Coins = "+str(coins))
        print("-----------")
        r = helper(maze, visited, coins, i+1, j, x, y, path+1)
        l = helper(maze, visited, coins, i-1, j, x, y, path+1)
        u = helper(maze, visited, coins, i, j+1, x, y, path+1)
        d = helper(maze, visited, coins, i, j-1, x, y, path+1)
        visited[i][j] = False
        return min(r, l, u, d)

    # initialize
    ans = 10000 # shortest path from starting location to target (so far)
    coins = 0 # total number of coins
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 2: 
                coins += 1
    visited = [[False] * len(maze[0])] * len(maze)
    # [0, 0]: current location
    # [x, y]: target location
    # 0: path length so far
    ans = helper(maze, visited, coins, 0, 0, x, y, 0)
    return ans if ans < 10000 else -1 

# Test the answers
if __name__ == '__main__':
    # should give 4
    maze = [[0, 2, 1], [1, 2, 0], [1, 0, 0]]
    x = 2
    y = 2
    ans = minMoves(maze, x, y)
    print(ans)
    """
    # should give 2
    maze = [[0, 2, 0], [0, 0, 1], [1, 1, 1]]
    x = 1
    y = 1
    ans = minMoves(maze, x, y)
    print(ans)

    # should give -1
    maze = [[0, 1, 0], [1, 0, 1], [0, 2, 2]]
    x = 1
    y = 1
    ans = minMoves(maze, x, y)
    print(ans)

    # should give 5
    maze = [[0, 2, 0], [1, 1, 2], [1, 0, 0]]
    x = 2
    y = 1
    ans = minMoves(maze, x, y)
    print(ans)
    """