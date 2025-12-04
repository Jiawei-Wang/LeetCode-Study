class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n, pos = len(S), -float('inf')
        res = [n] * n

        # forward loop
        for i in range(n):
            if S[i] == C:
                pos = i
            res[i] = min(res[i], abs(i - pos))

        # backward loop
        for i in range(n-1, -1, -1):
            if S[i] == C:
                pos = i
            res[i] = min(res[i], abs(i - pos))

        return res

        