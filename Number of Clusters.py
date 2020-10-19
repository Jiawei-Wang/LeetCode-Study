"""
Given a 2-d array , elements only consist of the lowecase alphabets - a , b or c.
Find the number of clusters (same lowecase alphabets that connect 4-directionally - up, down, left or right).
"""

class Solution:
    def clusters(self, grid):
        if not grid:
            return 0
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '#':
                    curr = grid[i][j]
                    count += 1
                    self.dfs(grid, i, j, curr)
        return count 

    def dfs(self, grid, i, j, curr):
        if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0])) or grid[i][j] != curr:
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j, curr)
        self.dfs(grid, i-1, j, curr)
        self.dfs(grid, i, j+1, curr)
        self.dfs(grid, i, j-1, curr)






if __name__ == "__main__":
    # test case 1: should return 2
    array = [
        ['a', 'a', 'a'],
        ['b', 'b', 'b']
    ]
    case = Solution()
    print(case.clusters(array))

    # test case 1: should return 3
    array = [
        ['b', 'b', 'b', 'c', 'a', 'a'],
        ['b', 'b', 'b', 'b', 'b', 'b']
    ]
    case = Solution()
    print(case.clusters(array))

    # test case 1: should return 6
    array = [
        ['a', 'a', 'a'],
        ['c', 'c', 'b'],
        ['a', 'b', 'a']
    ]
    case = Solution()
    print(case.clusters(array))