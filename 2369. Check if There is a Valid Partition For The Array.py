class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1) # dp[i] will be True if the prefix nums[:i] (first i elements) can be validly partitioned
        dp[0] = True  # empty prefix always “validly partitioned”

        # Check first possible partition of length 2
        if n >= 2 and nums[0] == nums[1]:
            dp[2] = True

        for i in range(3, n + 1):
            # Case: last two elements form a valid “2 equal” subarray
            if dp[i - 2] and nums[i - 2] == nums[i - 1]:
                dp[i] = True
            # Case: last three elements form a “3 equal” or “3 consecutive increasing” subarray
            elif dp[i - 3]:
                # three equal
                if nums[i - 3] == nums[i - 2] == nums[i - 1]:
                    dp[i] = True
                # three consecutive increasing
                elif nums[i - 3] + 1 == nums[i - 2] and nums[i - 2] + 1 == nums[i - 1]:
                    dp[i] = True

        return dp[n]