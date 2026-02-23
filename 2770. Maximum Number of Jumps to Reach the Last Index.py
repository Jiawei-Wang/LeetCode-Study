class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        # start from index = 0
        # each jump, I can reach any num in nums behind current num
        # with value: current - target <= num <= current + target
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0

        for index in range(1, n):
            curr = nums[index]
            low = curr - target
            high = curr + target

            for prev_idx in range(index):
                prev = nums[prev_idx]
                if low <= prev <= high and dp[prev_idx] != -1:
                    dp[index] = max(dp[index], dp[prev_idx] + 1)
        
        return dp[-1]