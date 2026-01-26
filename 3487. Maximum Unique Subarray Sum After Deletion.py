class Solution:
    def maxSum(self, nums: List[int]) -> int:
        total = 0
        has_positive = False
        biggest_negative = -float("inf")
        seen = set()
        for num in nums:
            if num in seen:
                continue
            elif num <= 0:
                biggest_negative = max(biggest_negative, num)
            else:                
                has_positive = True
                total += num
                seen.add(num)
        
        return total if has_positive else biggest_negative
        