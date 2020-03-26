class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 自我思路：Binary Tree的每个位置上的数值是固定的，所以只需要通过数学计算得出即可

        ans = []
        ans.insert(0, label)

        # 第一步：找到给出数字 label 的对应位置

        # （第 i 排的数字范围是 2^(i-1) 至 2^i - 1，以及每个偶数排数字顺序颠倒）
        row = 1;
        while label > 2**row - 1:
            row += 1
        if row % 2 == 1:
            column = label - (2**(row-1)) + 1
        else:
            column = 2**(row-1) - (label - (2**(row-1)) +1) + 1
        # 这样便得到 label 的值对应的位置：第row行第column个（从1开始计数）

        # 第二步：循环找出每个parent node的值
        while row > 1:
            row -= 1
            column = (column + 1)//2
            if row % 2 == 1:
                value = 2**(row-1) - 1 + column

            else:
                value = 2**(row-1) - 1 + (2**(row-1) - column + 1)
            ans.insert(0, value)

        #输出
        return ans
