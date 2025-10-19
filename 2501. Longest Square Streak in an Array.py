class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        available = set(nums)
        sorted_nums = sorted(available)
        longest = -1

        for num in sorted_nums:
            current_length = 0
            while num in available:
                available.remove(num)
                current_length += 1
                num *= num
            if current_length >= 2:
                longest = max(longest, current_length)
        
        return longest
            



