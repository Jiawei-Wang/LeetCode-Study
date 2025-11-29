# find number of times the array changes pattern (up to down, down to up)
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        length = len(nums)
        peak = 1 
        valley = 1

        # At every comparison between nums[i] and nums[i-1], we decide:
        # If it's going up, we extend a valley → new peak.
        # If it's going down, we extend a peak → new valley.
        for i in range(1, length):
            if nums[i] > nums[i-1]:
                peak = valley + 1
            elif nums[i] < nums[i-1]:
                valley = peak + 1
                
        return max(peak, valley)