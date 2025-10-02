class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = [0 for _ in range(len(grid))] # array to store info about each row
        col = [0 for _ in range(len(grid[0]))] # array to store info about each col
        server = set() # hashset to store all server locations

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
                    server.add((i,j))

        answer = len(server)
        for i, j in server:
            if row[i] == col[j] == 1: # if a server is on its own row and col
                answer -= 1
        return answer
