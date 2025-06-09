# sliding window
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeroes = 0 # how many zeroes in current subarray
        res = 0 # longest subarray so far
        start = 0 # start index

        # for each end index, move start index 
        # so that subarray meets requirements
        for end, num in enumerate(nums):
            if num == 0:
                zeroes += 1
            while zeroes > 1:
                if nums[start] == 0:
                    zeroes -= 1
                start += 1
            res = max(res, end - start) # this one solves corner case: all 1s in subarray, one must be deleted
        
        return res