# check all pairs: O(n^2 logm)
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_set = set(arr)
        
        def find_length(num1, num2):
            length = 2
            while num1 + num2 in arr_set:
                num1, num2 = num2, num1+num2
                length += 1
            return length if length >= 3 else 0

        best = 0
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                best = max(best, find_length(arr[i], arr[j]))
        return best


# improve upon the above answer with DP: O(n^2)
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)

        # Map value -> index for O(1) predecessor lookup
        index = {x: i for i, x in enumerate(arr)}

        # dp[j][i] = length of fib subsequence ending at indices (j, i)
        # Initialize all to 2 (minimum length before finding a valid chain)
        dp = [[2] * n for _ in range(n)]
        best = 0

        for i in range(n):
            for j in range(i):
                # We want some k such that:
                # arr[k] + arr[j] = arr[i]
                target = arr[i] - arr[j]

                # Since arr is strictly increasing:
                # target must be < arr[j], otherwise no valid k
                if target >= arr[j]:
                    continue

                # Find index k of target
                if target in index:
                    k = index[target]
                    dp[j][i] = dp[k][j] + 1
                    best = max(best, dp[j][i])

        # If best never updated, no valid subsequence (need length >= 3)
        return best if best >= 3 else 0
