class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        max_pen = total // cost1 
        result = 0
        for pen in range(0, max_pen + 1):
            remain = total - cost1 * pen
            max_pencil = remain // cost2
            result += max_pencil + 1
        return result
            