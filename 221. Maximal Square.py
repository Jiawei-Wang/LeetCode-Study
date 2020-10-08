# Brute Force
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        # cols不一定存在所以要保证有rows才去算cols，防止越界
        cols = len(matrix[0]) if rows else 0
        # 当前最佳答案
        maxsqlen = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    sqlen = 1
                    flag = True
                    # 如果没越界且上一层所有元素都是1
                    while sqlen + i < rows and sqlen + j < cols and flag:
                        # 遍历新的row和新的column，找到是否有0
                        for k in range(j, sqlen+j+1):
                            if matrix[i+sqlen][k] == '0':
                                flag = False
                                break
                        for k in range(i, sqlen+i+1):
                            if matrix[k][j+sqlen] == '0':
                                flag = False
                                break
                        # 如果在遍历完后每个元素依旧都是1,则往下方和右方扩一层
                        if flag:
                            sqlen += 1
                    # 更新最佳答案
                    if maxsqlen < sqlen:
                        maxsqlen = sqlen

        return maxsqlen * maxsqlen


# DP:
TODO 
