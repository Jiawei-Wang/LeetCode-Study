class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        # dp[i][j] = max sum of averages for first i elements split into j groups
        dp = [[0.0] * (k + 1) for _ in range(n + 1)]

        # Base case: 1 group → average of first i elements
        for i in range(1, n + 1):
            dp[i][1] = prefix[i] / i

        # Build up for j groups
        for j in range(2, k + 1): # number of groups, start from 2 since 1 is base case
            for i in range(j, n + 1): # how many numbers we are considering
                for p in range(j - 1, i): # the split point between last group and previous groups
                    dp[i][j] = max(dp[i][j], dp[p][j - 1] + (prefix[i] - prefix[p]) / (i - p))
                    # dp[p][j-1]: best sum using first p elements in j-1 groups
                    # (prefix[i] - prefix[p]) / (i - p)): average of the last group: nums[p:i]

        return dp[n][k]
