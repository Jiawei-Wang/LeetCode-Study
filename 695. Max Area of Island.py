# 读题时的疑惑：如何连续读取并记录 "1" ？

# DFS recursion
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        seen = set()

        def area(r, c):

            # 如果一个点不满足以下要求则停止
            # 范围在grid内 and 并未被遍历过 and 该点存在
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0

            # 标记已遍历的点
            seen.add((r, c))

            # recursion得出该点相邻四个点所拥有的面积并 +1
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        # 学习是用两个for的用法，遍历2d list中所有点，返回值最大的那个点
        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))

# 这个submit时间和内存消耗上都不够优秀

# DFS iterative
// TODO
