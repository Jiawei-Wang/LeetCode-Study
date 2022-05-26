# 难点：找到递增subsequence而不是subarray
# https://segmentfault.com/a/1190000003819886

# top down dp: dp[i]代表index=i处能获得的最长LIS，那么dp[i] = max(1, dp[i+1] if nums[i] < nums[i+1], dp[i+2] if nums[i] < nums[i+2], etc)
# time n^2: 因为dp[0]要找到其他所有符合条件的元素并取最大值+1
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)


# patient sorting
# tails：array storing the smallest tail of all increasing subsequences with length i+1 in tails[i]
# 举例：在[3,6,5,7]中长度为2的所有subsequence中（共有5个）末尾元素最小的的为[3,5]，所以tail[1] = 5
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size