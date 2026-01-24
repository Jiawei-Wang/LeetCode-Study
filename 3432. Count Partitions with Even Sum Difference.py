class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0

        count = 0
        for i in range(1, len(nums)):
            curr = nums[i]
            left += curr
            right -= curr
            if (right - left) % 2 == 0:
                count += 1
        return count