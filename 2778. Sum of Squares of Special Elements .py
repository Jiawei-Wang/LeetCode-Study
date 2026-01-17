class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for index, num in enumerate(nums):
            if n % (index+1) == 0:
                total += num * num
        return total
        