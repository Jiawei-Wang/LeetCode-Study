# brute force: n^2
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        
        # Check every starting point
        for i in range(n):
            target_count = 0
            # Expand to every ending point
            for j in range(i, n):
                if nums[j] == target:
                    target_count += 1
                
                # Check if it dominates strictly more than half of the subarray
                length = j - i + 1
                if target_count > length // 2:
                    ans += 1
                    
        return ans


# for every unique number in nums:
# if number == target: its weight = 1
# if number != target: its weight = -1
# then we can build a prefix sum where
# prefix[i] > 0 means target is majority in subarray 0 to i
# and prefix[j] - prefix[i] > 0 means target is majority in subarray i to j
# now the problem is: find all i, j pairs where prefix[i] < prefix[j]
# prefix sum has O(1) query but o(n) update
# Fenwick tree has o(logn) query and o(logn) update
# TODO: fenwirkc tree solution