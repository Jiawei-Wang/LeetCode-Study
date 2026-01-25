class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        # dp[a] will store the minimum operations needed to convert a -> y
        # initialize with -1 meaning "not computed yet"
        dp = [-1] * 10011

        def solve(a):
            # Base case:
            # If a <= y, the fastest way is only incrementing:
            # a -> a+1 -> ... -> y
            # which costs (y - a) operations
            if a <= y:
                return y - a

            # If we've already computed this state, reuse it
            if dp[a] != -1:
                return dp[a]

            # Worst case fallback:
            # Only use +/-1 operations directly from a to y
            # This gives an upper bound for the answer
            res = abs(a - y)

            # ---------------- Divide by 5 options ----------------

            # To divide by 5, a must be divisible by 5.
            # r is how far a is from the nearest lower multiple of 5.
            r = a % 5

            # Option 1: decrease a by r to make it divisible by 5,
            # then divide by 5.
            # Cost:
            #   r steps to subtract
            # + 1 step to divide
            # + recursively solve the smaller value (a // 5)
            res = min(res, 1 + r + solve(a // 5))

            # Option 2: increase a to the next multiple of 5,
            # then divide by 5.
            # (5 - r) steps to add
            # + 1 step to divide
            # result becomes (a // 5 + 1)
            res = min(res, 1 + (5 - r) + solve(a // 5 + 1))

            # ---------------- Divide by 11 options ----------------

            # Same idea for division by 11
            r = a % 11

            # Round down to nearest multiple of 11, then divide
            res = min(res, 1 + r + solve(a // 11))

            # Round up to next multiple of 11, then divide
            res = min(res, 1 + (11 - r) + solve(a // 11 + 1))

            # Store the result in dp to avoid recomputation
            dp[a] = res
            return res

        # Start recursion from x
        return solve(x)
