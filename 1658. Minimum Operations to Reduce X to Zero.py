# find longest subarray (in the middle) such that sum(subarray) == sum(whole array) - x
# sliding window
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        max_length = -1
        curr_sum = 0

        left = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while left <= right and curr_sum > total - x:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == total - x:
                max_length = max(max_length, right - left + 1)
        
        return len(nums) - max_length if max_length != -1 else -1

        