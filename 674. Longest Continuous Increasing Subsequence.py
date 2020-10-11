class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0: return 0
        count = 1
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count += 1
            else:
                ans = max(ans, count)
                count = 1
        return max(ans, count)