class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        free_move = 0
        standing = 0
        for move in moves:
            if move == "L":
                standing -= 1
            elif move == "R":
                standing += 1
            else:
                free_move += 1
        
        return abs(standing) + free_move