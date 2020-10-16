import math
import os
import random
import re
import sys

from itertools import permutations
from collections import deque

def minMoves(maze, endX, endY):
    col = len(maze[0])
    row = len(maze)
    """
    1. get list of all coins' locations
    """
    coin_list = []
    for i in range(row):
        for j in range(col):
            if maze[i][j] == 2:
                coin_list.append([i, j])
    k = len(coin_list)

    """
    2. make a 3d dp list: dp[i][j][k] = shortest distance from [i][j] to k-th coin 
       can get by using BFS starting from each coin
       row of dp = row of maze
       column of dp = column of maze
       3rd length of dp = len of coin_list
    """
    dp = [[[float('inf')] * k] * col] * row # initialize every distance to max
    for x in range(k): # for every coin
        coin_row = coin_list[x][0]
        coin_col = coin_list[x][1]

        # initialized every block as unvisited
        visited = [[False] * col] * row
        
        # bfs to get min distance of all blocks to this coin
        queue = deque() # append() and popleft()
        queue.append([coin_row, coin_col])
        visited[coin_row][coin_col] = True
        dp[coin_row][coin_col][x] = 0
        while queue:
            # get one element each time
            curr0, curr1 = queue.popleft() # curr is the location of current element
            for i, j in [[1,0],[-1,0],[0,1],[0,-1]]: # for all its 4 neighbors
                # within range, not visited, cannot be 1 (wall)
                if (curr0+i < 0 or curr0+i >= row or curr1+j < 0 or curr1+j >= col) or visited[curr0+i][curr1+j] == True or maze[curr0+i][curr1+j] == 1:
                    continue
                else:
                    queue.append([curr0+i, curr1+j])
                    visited[curr0+i][curr1+j] = True
                    dp[curr0+i][curr1+j][x] = dp[curr0][curr1][x] + 1

    """
    3. get every possible order of coins by using itertools
    """
    # coin_list: a list, each element is a location pair of a coin: [i, j]
    # combination: a list of all possible orders, each element is a tuple of all coins:
    # for example if 2 coins: [(coin1, coin2), (coin2, coin1)]
    # improve: use index of coin rather than coin location
    combination = list(permutations(i for i in range(len(coin_list))))

    """
    4. calculate all (starting point to all coins to target point) distances, choose min one
    
    every element in combination is a tuple of travel order: start -> first element in tuple -> ... -> last -> target
    if cost of any part is inf, then total distance of this tuple is inf
    """
    ans = float('inf')
    dist_list = []
    for order in combination: # order is a tuple of index of coins in coin_list
        dist = dp[0][0][order[0]] # initilize distance = [0][0] to first coin in order
        tail = dp[endX][endY][order[-1]] # from last coin to target

        # if cannot reach first coin, dist is inf
        if dist == float('inf') or tail == float('inf'):
            dist_list.append(float('inf'))
            continue

        # add distance of every coin
        for i in range(1, len(order)):
            x = coin_list[order[i-1]][0]
            y = coin_list[order[i-1]][1]
            z = order[i]
            
            # if distance between order[i-1] and order[i] is inf, total dist is inf
            if dp[x][y][z] == float('inf'):
                dist_list.append(float('inf'))
                break
            else:
                dist += dp[x][y][z]
        
        total = dist + tail
        dist_list.append(total)
    ans = min(dist_list)
    return ans if ans != float('inf') else -1

if __name__ == '__main__':
    # return 2
    maze = [
        [0, 2, 0],
        [0, 0, 1],
        [1, 1, 1]
    ]
    endX = 1
    endY = 1
    ans = minMoves(maze, endX, endY)
    print("--------------")
    print("Answer should be: 2")
    print("return answer: ")
    print(ans)
"""
    # return -1
    maze = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 2, 2]
    ]
    endX = 1
    endY = 1
    ans = minMoves(maze, endX, endY)
    print("--------------")
    print("Answer should be: -1")
    print(ans)

    # return 5
    maze = [
        [0, 2, 0],
        [1, 1, 2],
        [1, 0, 0]
    ]
    endX = 2
    endY = 1
    ans = minMoves(maze, endX, endY)
    print("--------------")
    print("Answer should be: 5")
    print(ans)

    # return 4
    maze = [
        [0, 2, 1],
        [1, 2, 0],
        [1, 0, 0]
    ]
    endX = 2
    endX = 2
    ans = minMoves(maze, endX, endY)
    print("--------------")
    print("Answer should be: 4")
    print(ans)
"""