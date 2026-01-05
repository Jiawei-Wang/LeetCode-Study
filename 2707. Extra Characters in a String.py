class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [0] * (n + 1)

        for i in range(n):
            # Case 1: treat s[i] as extra char
            dp[i + 1] = dp[i] + 1

            # Case 2: match dictionary words ending at i
            for word in dictionary:
                lw = len(word)
                if i - lw + 1 >= 0 and s[i - lw + 1 : i + 1] == word:
                    dp[i + 1] = min(dp[i + 1], dp[i - lw + 1])

        return dp[n]
