class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        biggest = -float("inf")
        second = -float("inf")

        for num in nums:
            if num > biggest:
                biggest, second = num, biggest
            elif num == biggest:
                second = num
            elif num > second:
                second = num
        
        return (biggest-1) * (second-1)