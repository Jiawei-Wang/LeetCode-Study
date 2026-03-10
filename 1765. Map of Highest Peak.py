class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row = len(isWater)
        col = len(isWater[0])

        # 1. mark water block as 0 and land block as 9999999, in place
        # 2. also store all water block in array
        pending = []
        for r in range(row):
            for c in range(col):
                if isWater[r][c] == 0:
                    isWater[r][c] = 9999999
                else:
                    isWater[r][c] = 0
                    pending.append((r,c))
        
        def is_land(index):
            r = index[0]
            c = index[1]
            if 0 <= r < row and 0 <= c < col and isWater[r][c] != 0:
                return True

        # start from all water blocks, bfs to increase neighbor blocks by 1
        visited = set()
        while pending:
            nxt = []
            for current in pending:
                if current in visited:
                    continue

                r = current[0]
                c = current[1]
                visited.add((r,c))
                height = isWater[r][c]

                # every current block has 4 neighbors
                for i, j in [(1,0), (-1,0), (0,1), (0,-1)]:
                    neighbor = (r+i, c+j)
                    if is_land(neighbor):
                        nxt.append(neighbor)
                        isWater[r+i][c+j] = min(isWater[r+i][c+j], height+1)
            pending = nxt

        return isWater


