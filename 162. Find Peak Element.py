# when there are no two equal value neighbors
# it is guaranteed to have at least one peak element
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0
        
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n-1
        """
        the above part serves two purposes:
        1. clean the corner cases so no messy code in the main loop
        2. guarantee there is at least one answer between start and end 
        (because it's increasing at the beginning and decreasing at the end)
        """

        start = 1
        end = n-2
        while start <= end:
            mid = start + (end-start)//2
            # mid has 3 possible positions: 
            # on the increasing slop
            # on the decreasing slop
            # at the peak
            # we don't know how many mountians in the whole array
            # but mid is on one of them
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid-1]:
                end = mid-1
            elif nums[mid] < nums[mid+1]:
                start = mid+1
        