# 0 <= rowCosts[r], colCosts[c]
# so a block will not be visited twice
# looking only at the rows
# the shorest path is from startPos directly to homePos
# same for cols
# so every shortest path shares the same total sum
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        res = 0
        [i, j] = startPos
        [x, y] = homePos

        def cmp(a, b):
            return (a > b) - (a < b) 

        while i != x:
            i += cmp(x, i)
            res += rowCosts[i]
        while j != y:
            j += cmp(y, j)
            res += colCosts[j]
        return res