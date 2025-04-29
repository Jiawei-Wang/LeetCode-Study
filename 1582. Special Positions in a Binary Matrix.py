# brute force: scan everything 
# m*n*(m+n)
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        count = 0

        def check(i, j):
            for index in range(col):
                if mat[i][index] == 1 and index != j:
                    return False
            for index in range(row):
                if mat[index][j] == 1 and index != i:
                    return False
            return True

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 1 and check(i,j):
                    count += 1
        
        return count


# two pass
# time m*n
# space m+n
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # first pass count number of 1s
        rows = [0] * len(mat)
        cols = [0] * len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    rows[i] += 1
                    cols[j] += 1

        # second pass check if it's along in the corresponding row and col
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] and rows[i] == 1 and cols[j] == 1:
                    res += 1

        return res