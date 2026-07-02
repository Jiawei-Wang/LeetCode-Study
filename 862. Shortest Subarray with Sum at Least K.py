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
        


# sliding window (n) from leetcode 209 can't solve this problem because of negative numbers
# go back to using prefix sum: 
# find two indices such that prefix[i] - prefix[j] >= k, and make i-j as small as possible
# we also can't do binary search with prefix sum (nlogn) for same reason 
# if we check every pair using prefix sum, that is n^2
# so to make it faster, we need to check for repetitive computation
# 1. where is the repetitive computation
# imagine we have a valid pair j, i such that prefix[i] - prefix[j] >= k
# then subarray length = i - j
# and we move onto next index i+1
# if prefix[i+1] - prefix[j] >= k, then subarray length = i+1 - j > i - j
# therefore same index j will never be the starting index for a shorter subarray
# so there is no reason to use j anymore for future end index i
# 2. how do we eliminate redundancy 
# 1) a starting index j should be removed when we find a valid end index i
# (i only becomes bigger so the first valid one is already the best one)
# 2) also if new index j2 has prefix[j2] <= prefix[j1] for old index j1
# j2 will always be a better starting index for any i, compared to j1
# then we can get rid of j1
# in order to keep track of them
# we add deque as a pool of candidate that can be the starting pointer j
from collections import deque

class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        # Step 1: pre compute prefix.
        # B[i] represents the sum of nums[0] up to nums[i-1].
        # We need size n + 1 to handle subarrays that start from index 0.
        n = len(nums)
        B = [0] * (n + 1)
        for i in range(n):
            B[i + 1] = B[i] + nums[i]
            
        # d will store the indices of the prefix sum array.
        # It acts as our "pool of starting candidates".
        d = deque()
        min_length = n + 1 # Initialize with a value larger than any possible answer
        
        # Step 2: Iterate through all prefix sums
        for i in range(n + 1):
            
            # --- LOOP 1: CLAIMING VICTORIES ---
            # Check if the current prefix sum minus the oldest candidate's 
            # prefix sum satisfies the target K.
            while d and B[i] - B[d[0]] >= k:
                # If valid, calculate the window length and update our minimum.
                min_length = min(min_length, i - d.popleft())
                # We popleft() because this index `i` is the closest possible 
                # endpoint for `d[0]`. Any future endpoint would just be farther away.
                
            # --- LOOP 2: ELIMINATING OBSOLETE CANDIDATES ---
            # Before adding the current index `i`, check the back of the deque.
            # If an older candidate has a prefix sum greater than or equal to B[i],
            # it is no longer useful.
            while d and B[i] <= B[d[-1]]:
                d.pop()
                # We pop() because index `i` is a better starting candidate than `d[-1]`:
                # 1. It is further to the right (can yield shorter future subarrays).
                # 2. Its prefix sum is smaller (yields a larger or equal subarray sum).
            
            # so for each step, we look into the deque from both directions
            # and try to remove worse starting index candidates
            # only after all these are done will we add the current index to our pool of candidates
            d.append(i)
            
        # If min_length was never updated, it means no valid subarray was found.
        return min_length if min_length <= n else -1