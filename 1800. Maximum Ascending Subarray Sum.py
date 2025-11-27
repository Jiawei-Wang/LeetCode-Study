class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        best = 0
        for left in range(len(nums)):
            total = nums[left]
            right = left + 1
            while right < len(nums) and nums[right] > nums[right - 1]:
                total += nums[right]
                right += 1
            best = max(best, total)
        return best

