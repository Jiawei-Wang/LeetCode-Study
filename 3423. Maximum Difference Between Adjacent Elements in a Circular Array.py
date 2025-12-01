class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        answer = 0
        for i in range(0, len(nums)-1):
            answer = max(answer, abs(nums[i]-nums[i+1]))
        answer = max(answer, abs(nums[-1]-nums[0]))
        return answer