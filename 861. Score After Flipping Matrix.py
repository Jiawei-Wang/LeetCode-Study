class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        # 读题后第一想法：
        # 其实这道题可以转化为：如何让2D list中的“1”尽可能多（但是也不尽然，1数量相同的情况下越靠左越好）
        # 主要的难点在于：如何翻可以得到最大可能结果


        # 第一次尝试：
        # 保持循环直到没法得到更大的数字
        # 所有数字的权重均相同，每个数字前一位的“1”的权重大于后面所有之和，所以优先保证前面的“1”
        # 具体算法：首先看row，如果第一位有0，则翻转，然后看column，如果0多于1,则翻转，然后重复
        def row(i):
            for index in range(len(i)):
                if i[index] == 1:
                    i[index] = 0
                else:
                    i[index] = 1
            return i


        def column(A):
            # 修改column
            # 读取一列，计算0和1哪个多，是否翻转，并重复len(A[0])次
            for j in range(len(A[0])):
                count = 0
                for i in range(len(A)):
                    if A[i][j] == 1:
                        count += 1
                    else:
                        count -= 1
                if count < 0:
                    for i in range(len(A)):
                        if A[i][j] == 1:
                            A[i][j] = 0
                        else:
                            A[i][j] = 1



        for i in A:
            if i[0] == 0:
                row(i)
        column(A)

        ans = 0
        for i in A:
            binary = ''.join(str(e) for e in i)
            ans += int(binary, 2)
        return ans

    # Time: 98%
    # Space: 20%
