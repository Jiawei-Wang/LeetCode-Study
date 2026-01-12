"""
always pair current min with current max

prove:
    assume curr_min <= i, j <= curr_max
    then max(curr_min + curr_max, i + j) <= max(curr_min + i, curr_max + j)
    so for each round, pair current min with current max
    the result is optimal 
"""
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer = -float("inf")
        for i in range(len(nums)//2):
            answer = max(answer, nums[i]+nums[-1-i])
        return answer

        