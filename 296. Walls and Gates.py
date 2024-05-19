"""
you are given an m*n grid rooms initialized with these three possible values
-1: A wall or an obstacle
0: A gate
INF: infinity means an empty room

fill each empty room with the distance to its nearest gate, 
if it is impossible to reach a gate, it should be filled with INF

example:
rooms = [
    [inf,  -1,   0,    inf],
    [inf,  inf,  inf,  -1],
    [inf,  -1,   inf,  -1],
    [0,    -1,   inf,  inf]
]

find the shortest distance between an inf and any 0, if inf is reachable
"""

# BFS from all 0s
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        
        # helper function to update data structures when we visit a new location
        def addRooms(r, c):
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or rooms[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])
        
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        # first we find all 0s
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        # then we bfs on all other locations 
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            dist += 1