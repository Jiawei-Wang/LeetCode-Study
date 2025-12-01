# TLE
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        count = 0

        def backtrack(index, total):
            nonlocal count

            if index == n:          # must use ALL n dice
                if total == target:
                    count = (count + 1) % MOD
                return

            if total > target:      # prune
                return

            # try all k faces
            for face in range(1, k + 1):
                backtrack(index + 1, total + face)

        backtrack(0, 0)
        return count


# dp(d, f, target) = dp(d-1, f, target-1) + dp(d-1, f, target-2) + ... + dp(d-1, f, target-f)
# The base case occurs when d = 0. We can make target=0 with 0 dice, but nothing else.
# So dp(0, f, t) = 0 iff t != 0, and dp(0, f, 0) = 1.
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}

        def dp(n, target):
            if n == 0:
                return 0 if target > 0 else 1
            if (n, target) in memo:
                return memo[(n, target)]
            combo = 0
            for face in range(max(0, target-k), target):
                combo += dp(n-1, face)
            memo[(n, target)] = combo
            return combo
        
        return dp(n, target) % (10**9 + 7)