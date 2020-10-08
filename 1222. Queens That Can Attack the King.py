class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        # 使用tuple和set的组合来提高查询速度，同时也可去除重复元素
        queens = {(i, j) for i, j in queens}

        # 一共有8个方向，每个方向至多走7步
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in range(1, 8):
                    x, y = king[0] + i * k, king[1] + j * k
                    # 找到第一个即可退出该层循环
                    if (x, y) in queens:
                        res.append([x, y])
                        break
        return res
