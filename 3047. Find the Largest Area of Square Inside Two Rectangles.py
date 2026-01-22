class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        ans = 0

        for i in range(n):
            x1, y1 = bottomLeft[i]
            x2, y2 = topRight[i]

            for j in range(i + 1, n):
                x3, y3 = bottomLeft[j]
                x4, y4 = topRight[j]

                overlap_w = min(x2, x4) - max(x1, x3)
                overlap_h = min(y2, y4) - max(y1, y3)

                if overlap_w > 0 and overlap_h > 0:
                    side = min(overlap_w, overlap_h)
                    ans = max(ans, side * side)

        return ans