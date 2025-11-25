class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count_neg = 0
        count_zero = 0
        for num in nums:
            if num < 0:
                count_neg += 1
            elif num == 0:
                count_zero += 1
            else:
                break
        return max(count_neg, len(nums)-count_neg-count_zero)
        