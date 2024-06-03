class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)} # set((0,0)) will result in {0}
        x = 0
        y = 0
        for char in path:
            print(visited)
            if char == "N":
                y += 1
            elif char == "S":
                y -= 1
            elif char == "W":
                x -= 1
            else:
                x += 1
            if (x, y) in visited:
                return True
            else:
                visited.add((x,y))
        
        return False
