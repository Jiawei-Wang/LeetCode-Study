# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/solutions/117723/python-standard-dp-solution-with-explanation
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        dp = 0 
        prev = -1
        answer = 0
        
        for i in range(len(nums)):
            if nums[i] < left and i != 0:
                answer += dp
            elif nums[i] > right:
                dp = 0
                prev = i
            elif left <= nums[i] <= right:
                dp = i - prev
                answer += dp
        
        return answer