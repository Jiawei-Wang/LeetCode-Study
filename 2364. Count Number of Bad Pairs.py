# if we choose to find good pairs instead of bad pairs, we just need to find where j - i == nums[j] - nums[i]
# even easier if we want to find where j - nums[j] == i - nums[i]
# now the question becomes: for each i - nums[i], check how many times we have seen it before
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)

        total_pairs = n * (n-1) // 2
        good_pairs = 0
        dp = dict()

        for i, num in enumerate(nums):
            target = i - num
            good_pairs += dp.get(target, 0)
            dp[target] = dp.get(target, 0) + 1
        
        return total_pairs - good_pairs
