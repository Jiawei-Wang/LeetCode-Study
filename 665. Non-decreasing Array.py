# 解法1：brute force，挨个修改array A中的元素，查看array是否符合要求
# Time: n^2
# Space: n
class Solution:
    def checkPossibility(self, A):

        # helper：检查输入array是否是non decreasing，如果不是，返回False
        def monotone_increasing(arr):
            for i in range(len(arr) - 1):
                if arr[i] > arr[i+1]:
                    return False
            return True

        new = A[:]
        for i in range(len(A)):
            # 使用变量暂存原始数据
            old_ai = A[i]
            # 如果是0号元素，则设为无穷小
            new[i] = new[i-1] if i > 0 else float('-inf')
            # 如果通过修改一个元素，使得array符合要求，则返回True
            if monotone_increasing(new):
                return True
            # 把被修改的元素还原
            new[i] = old_ai

        return False
