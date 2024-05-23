"""
Binary search:
1. for all ways we can divide an array: 
   (value of the largest subarry) will be between [max(nums) and sum(nums)] (inclusive)
2. instead of going through all possible ways to find 
   the smallest (value of the largest subarray) within all valid ways
   we pick (value of the largest subarray) and see if the value is feasible
3. we pick mid value within current range
3. each time use greedy to check:
    1) start from left and expand the current subarray
    2) find a cut point where current subarray <= mid
    3) at the end we will find either we can divide array into <= k subarrays or not
        1- if we can: true answer <= mid
        2- if we cannot: true answer > mid
"""
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k == 1:
            return sum(nums)
        
        def valid(target):
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > target:
                    total = num
                    count += 1
                    if count > k:
                        return False
            return True

        l = max(nums)
        r = sum(nums)
        while l <= r:
            mid = l + (r-l)//2
            if valid(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

        """
        1. if 3 values left: l + 1 = mid = r - 1: go into 1
        2. if 2 values left: l = mid = r - 1: stop or go into 1
        3. if 1 value left: l = mid = r: stop 
        """

        