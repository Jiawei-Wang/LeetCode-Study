class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        stack = []
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                dp[i] = max(dp[i] + 1, dp[stack.pop()])
            stack.append(i)
        return max(dp)