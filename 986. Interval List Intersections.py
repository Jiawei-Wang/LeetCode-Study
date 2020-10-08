class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # The solution is pretty simple. There is guaranteed to be an overlap interval if:
        # A[i].start <= B[j].end and B[j].start <= A[i].end

        m, n = len(A), len(B)
        i = j = 0
        res = []
        while i < m and j < n:
            if A[i][-1] >= B[j][0] and A[i][0] <= B[j][-1]:
                res.append([max(A[i][0], B[j][0]), min(A[i][-1], B[j][-1])])

            # 一次只移动一对中的小的那个的pointer
            if A[i][-1] < B[j][-1]:
                i += 1
            else:
                j += 1
        return res 
