"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

# go across a matrix where x is the row and y is the column
# find all elements in matrix where value equals to z
# any matrix[x][y] < matrix[x+1][y]
# any matrix[x][y] < matrix[x][y+1]
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        y = 1000 # start from top right corner
        for x in range(1, 1001): # scan row by row
            while y > 1 and customfunction.f(x, y) > z: 
                y -= 1 # move to left column
            if customfunction.f(x, y) == z:
                res.append([x, y])
        return res