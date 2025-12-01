# if we take m moves to make every number the same:
# target * len(nums) = sum(nums) + m * (len(nums) - 1)
# and 
# target = min(nums) + m
# (regardless which len(nums) - 1 numbers we pick for each round of increment
#  the minimum number will always be part of the pick, so it will always stay
#  as the minimum number, therefore target is m steps away from min(nums))
# so
# sum(nums) - min(nums) * len(nums) = m 
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)
        