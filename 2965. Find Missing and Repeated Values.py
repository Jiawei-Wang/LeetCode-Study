class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        hashset = set([x for x in range(1, n*n+1)])
        a = None
        b = None
        for i in range(n):
            for j in range(n):
                current = grid[i][j]
                if current in hashset:
                    hashset.remove(current)
                else:
                    a = current
        b = list(hashset)[0]
        return [a, b]