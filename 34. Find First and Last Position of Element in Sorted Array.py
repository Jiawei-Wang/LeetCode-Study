# two binary search for two indexes
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]
        
    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums)-1
        i = -1 # if i doens't exist return -1
        while l <= r:
            m = (r-l)//2 + l
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                # move l and r depending on which index is asked for 
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i