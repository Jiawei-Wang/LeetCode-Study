class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist = float("inf")
        ans = -1

        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                d = abs(a - x) + abs(b - y)
                if d < min_dist:
                    min_dist = d
                    ans = i
                # if d == min_dist: do nothing, since we want the one with smallest index

        return ans
