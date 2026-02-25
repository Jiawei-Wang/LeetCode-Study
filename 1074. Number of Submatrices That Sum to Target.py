"""
brute force: 
1. for every top-left bottom-right pair: col^2 * row*2
2. sum all elements inside: col * row
in total: col^3 * row^3

start by optimizing step 2: use prefix sum to get sum faster:
if we pre-calculate a 2d prefix sum where 
pref[r][c] = sum of all elements from [0,0] to [r,c], then query is O(1)
so we only need to go through ever top-left bottom-right pair
in total: col^2 * row^2

finally optimize picking every top-left bottom-right pair part:
instead of picking all 4 indexes: top, left, bottom, right
we only pick 3 indexes: left column i, right column j, and a sliding row scan
for each left/right column pair: scan through all rows to find target
in total: col^2 * row
"""

# apply idea from leetcode 560
# prefix sum: O(col^2 * row)
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
        # prefix sum for each row 
        for row in matrix:
            for i in range(1, n):
                row[i] += row[i-1] # do this in space since we don't need the input matrix anymore
        
        res = 0
        # for all possible column pairs
        for i in range(n):
            for j in range(i, n):
                hashmap = defaultdict(int)
                hashmap[0] += 1 # 1 way to get 0: empty array
                cur = 0
                # for each row, apply the same logic as leetcode 560
                for k in range(m):
                    # calculate sum of elements between column i and j on row k
                    cur += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    # check to see if there is any previous sum that can help get to target
                    res += hashmap[cur - target] 
                    hashmap[cur] += 1
    
        return res
        # essentially we pre compute prefix sum for each whole row
        # that enables us to get sum of elements between column i and j on each row quickly
        # to save space: store them in place
        # then compute prefix sum for combined rows during iterations