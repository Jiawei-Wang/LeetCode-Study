class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == 'R': dx, dy = dy, -dx
            if i == 'L': dx, dy = -dy, dx
            if i == 'G': x, y = x + dx, y + dy

        # if robot goes back to 0,0 after instructions, it is a loop
        # otherwise, if it ends NOT facing north, 
        # it is either half of the loop or 1/4 or the loop
        return (x, y) == (0, 0) or (dx, dy) != (0,1)