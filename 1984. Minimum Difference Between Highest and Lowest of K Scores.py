class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = float('inf')
        for i in range(k-1, len(nums)):
            answer = min(answer, nums[i]-nums[i-k+1])
        return answer
