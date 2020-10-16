import math
import os
import random
import re
import sys

from itertools import permutations
from collections import deque

def minMoves(maze, x, y):
    """
    1. get list of all coins' locations
    """
    coin_list = []
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 2:
                coin_list.append([i, j])

    """
    2. make a 3d dp list: dp[i][j][k] = shortest distance from [i][j] to k-th coin 
       can get by using BFS starting from each coin
       row of dp = row of maze
       column of dp = column of maze
       3rd length of dp = len of coin_list
    """
    k = len(coin_list)
    col = len(maze[0])
    row = len(maze)
    dp = [[[0] * k] * col] * row # initialize every distance as 0
    for x in range(len(coin_list)): # for every coin
        # bfs to get min distance of all blocks to this coin
        queue = deque()
        queue.append(coin_list[x])
        while queue:
            TODO







    """
    3. get every possible order of coins by using itertools
    """
    # coin_list: a list, each element is a location pair of a coin: [i, j]
    # combination: a list of all possible orders, each element is a tuple of all coins:
    # for example if 2 coins: [(coin1, coin2), (coin2, coin1)]
    combination = list(permutations(coin_list))

    """
    4. calculate all (starting point to all coins to target point) distances, choose min one
    """
    TODO
    return 3


if __name__ == '__main__':
    # return 2
    maze = [
        [0, 2, 0],
        [0, 0, 1],
        [1, 1, 1]
    ]
    x = 1
    y = 1
    ans = minMoves(maze, x, y)
    print("--------------")
    print("Answer should be: 2")
    print(ans)

    # return -1
    maze = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 2, 2]
    ]
    x = 1
    y = 1
    ans = minMoves(maze, x, y)
    print("--------------")
    print("Answer should be: -1")
    print(ans)

    # return 5
    maze = [
        [0, 2, 0],
        [1, 1, 2],
        [1, 0, 0]
    ]
    x = 2
    y = 1
    ans = minMoves(maze, x, y)
    print("--------------")
    print("Answer should be: 5")
    print(ans)

    # return 4
    maze = [
        [0, 2, 1],
        [1, 2, 0],
        [1, 0, 0]
    ]
    x = 2
    y = 2
    ans = minMoves(maze, x, y)
    print("--------------")
    print("Answer should be: 4")
    print(ans)