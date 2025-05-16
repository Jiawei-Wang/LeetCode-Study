# dp
class Solution:
    def numSquares(self, n: int) -> int:
        # cntPerfectSquares[i] = the least number of perfect square numbers that sum to i
        cntPerfectSquares = [float('inf')] * (n + 1)
        cntPerfectSquares[0] = 0

        for i in range(1, n + 1):
            # check all possible j
            j = 1
            while j * j <= i:
                cntPerfectSquares[i] = min(cntPerfectSquares[i], cntPerfectSquares[i - j * j] + 1)
                j += 1

        return cntPerfectSquares[n]


# improved dp with static cache
class Solution:
    cntPerfectSquares = [0]  # static-like class-level cache

    def numSquares(self, n: int) -> int:
        while len(Solution.cntPerfectSquares) <= n:
            i = len(Solution.cntPerfectSquares)
            cntSquares = float('inf')
            j = 1
            while j * j <= i:
                cntSquares = min(cntSquares, Solution.cntPerfectSquares[i - j * j] + 1)
                j += 1
            Solution.cntPerfectSquares.append(cntSquares)

        return Solution.cntPerfectSquares[n]