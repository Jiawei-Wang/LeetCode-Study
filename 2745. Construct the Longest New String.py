"""
x: # of "AA"
y: # of "BB"
z: # of "AB"
find length of longest string we can construct without having any "AAA" or "BBB"

thinking:
1. no "AAA" and no "BBB" means: 
    "AA" must be followed by "BB"
    "BB" must be followed by "AA" or "AB"
    "AB" must be followed by "AA" or "AB"
2. so question becomes:
    maximum number of stage 1, stage 2, stage 3 we can get into, by following the rules:
    1 can go into 2
    2 can go into 1 or 3
    3 can go into 1 or 3
    and we can at most go into x 1, y 2 and z 3
3. DP should be the answer
"""
class Solution:
    def __init__(self):
        # 1 <= x, y, z <= 50
        # Initialize a 4D dp table with dimensions [51][51][51][4]
        self.dp = [[[[0 for _ in range(4)] for _ in range(51)] for _ in range(51)] for _ in range(51)]
        # dp[x][y][z][last]: how many stage 1, 2, 3 left and which one is the last stage

    def solve(self, x, y, z, last):
        if self.dp[x][y][z][last] != 0:
            return self.dp[x][y][z][last]

        res = 0
        if x > 0 and last != 1: # stage 1 follows 2 or 3
            res = max(res, 2 + self.solve(x - 1, y, z, 1))
        if y > 0 and last <= 1: # stage 2 follows 1
            res = max(res, 2 + self.solve(x, y - 1, z, 2))
        if z > 0 and last != 1: # stage 3 follows 2 or 3
            res = max(res, 2 + self.solve(x, y, z - 1, 3))
        # above code can deal with initial stage 0

        self.dp[x][y][z][last] = res
        return res

    def longestString(self, x, y, z):
        return self.solve(x, y, z, 0) # start from stage 0


# math
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        mn = min(x, y)
        if x == y:
            return 4 * x + 2 * z
        else:
            return 2 * mn + (mn + 1) * 2 + 2 * z
  