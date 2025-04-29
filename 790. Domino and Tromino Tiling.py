class Solution:
    def numTilings(self, N: int) -> int:
        md = int(1e9) + 7
        v = [0] * 1001
        v[1] = 1
        v[2] = 2
        v[3] = 5
        if N <= 3:
            return v[N]
        for i in range(4, N + 1):
            v[i] = 2 * v[i - 1] + v[i - 3]
            v[i] %= md
        return v[N]
    

class Solution:
    def numTilings(self, n: int) -> int:
        md = int(1e9) + 7
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5

        dp1, dp2, dp3 = 1, 2, 5
        for _ in range(4, n + 1):
            dp4 = (2 * dp3 + dp1) % md
            dp1, dp2, dp3 = dp2, dp3, dp4

        return dp3