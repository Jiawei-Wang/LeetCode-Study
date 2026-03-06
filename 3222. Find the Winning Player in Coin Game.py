# 115 = 75 + 10 * 4
class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        move = 0
        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            move += 1
        if move % 2:
            return "Alice"
        else:
            return "Bob"


class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        move = min(x, y//4)
        if move % 2:
            return "Alice"
        else:
            return "Bob"