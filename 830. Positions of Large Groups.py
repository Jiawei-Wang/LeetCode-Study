class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        i, j, N = 0, 0, len(S)
        res = []
        while i < N:
            while j < N and S[j] == S[i]: 
                j += 1
            if j - i >= 3: 
                res.append([i, j - 1])
            i = j
        return res


        