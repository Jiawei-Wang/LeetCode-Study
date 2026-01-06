class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (high + 1)
        # dp[i] = number of ways to build a string of length i
        dp[0] = 1

        for length in range(1, high + 1):
            if length >= zero:
                dp[length] = (dp[length] + dp[length - zero]) % MOD
            if length >= one:
                dp[length] = (dp[length] + dp[length - one]) % MOD

        answer = 0
        for i in range(low, high + 1):
            answer = (answer + dp[i]) % MOD
        return answer
