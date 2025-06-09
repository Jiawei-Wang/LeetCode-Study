class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs) # in total n strings
        col = len(strs[0]) # each string is of length col

        answer = 0
        for c in range(col):
            target = strs[0][c]
            for i in range(1, n):
                if strs[i][c] < target:
                    answer += 1
                    break
                else:
                    target = strs[i][c]
        
        return answer

