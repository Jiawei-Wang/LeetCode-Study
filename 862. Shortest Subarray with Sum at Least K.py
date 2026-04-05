"""
0. we can't use sliding window since numbers can be negative
so we don't know when to expand or shrink the window 

1. we can still use prefix sum for fast check
create prefix sum array P
so sum of subarray l to r is P[r] - P[l]
goal: find minimum (r-l) such that P[r] - P[l] >= k

2. now the issue is: 
while iterating through r, how to find l fast

imagine we are checking two left indices l1 and l2, l1 < l2
if P[l2] <= P[l1], then l1 is now completely useless, because
for current r and any future r:
    1) P[r] - P[l2] >= P[r] - P[l1]
    2) r - l2 < r - l1
so if we find a smaller previx sum, we remove the older larger ones 
this will give us a monotonically increasing array, this can be done with a stack
by popping from behind

there are still some repeatitive computations:
if we get a valid pair l and r1, any future r2 that can pair with l will have:
r2 - l > r1 - l, so l is not needed anymore
this can be done with a queue by popping from front

therefore, we use deque
"""
from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Create Prefix Sums (length n + 1)
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
            
        dq = deque()
        min_len = float('inf')
        
        for i, curr_sum in enumerate(prefix_sums): 
            # first if we want to use i as left index
            # check for older and bigger prefix sums
            # since for future right index
            # i is better so we won't need them anymore
            while dq and curr_sum <= prefix_sums[dq[-1]]:
                dq.pop()
            
            # second if we want to use i as right index
            # scan through array to find the shortest valid subarray
            # and also remove obsolete ones along the way
            while dq and curr_sum - prefix_sums[dq[0]] >= k:
                min_len = min(min_len, i - dq.popleft())
            
            dq.append(i)
            
        return min_len if min_len != float('inf') else -1
        