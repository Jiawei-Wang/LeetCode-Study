class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target and maxDoubles:
            if target % 2:
                target -= 1
            else:
                maxDoubles -= 1
                target //= 2
            res += 1
        return res + target - 1
