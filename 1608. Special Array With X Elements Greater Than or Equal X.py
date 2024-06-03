class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        def helper(x):
            if x <= nums[0]:
                return len(nums)
            elif x > nums[-1]:
                return 0
                
            lo = 0
            hi = len(nums)-1
            while lo < hi:
                mid = lo + (hi-lo)//2
                if nums[mid] >= x:
                    hi = mid
                else:
                    lo = mid + 1
            return len(nums) - lo

        for x in range(0, len(nums)+1):
            if x == helper(x):
                return x
        return -1



        