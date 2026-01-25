class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        max1 = -1000
        max2 = -1000
        min1 = 1000

        for x in nums:
            if x > max1:
                max2 = max1
                max1 = x
            elif x > max2:
                max2 = x

            if x < min1:
                min1 = x

        return max1 + max2 - min1
