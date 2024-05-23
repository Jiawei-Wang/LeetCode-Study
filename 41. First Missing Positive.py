# For nums with length n, the possible result is in the range of
# [1 : n + 1], we want to know the smallest integer in the range 
# of [1 : n] that is not in nums, if [1 : n] are all in nums,
# the result is n + 1

# solution 1: use a set 
# time n space n
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        target = set(x for x in range(1, len(nums)+2))
        for num in nums:
            if num in target:
                target.remove(num)
        return min(target)


# solution 2: modify directly on input array
# time n space 1
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # logic: 
        # in order to save the extra space, we want to modify on input array
        # without losing original information
        # so we choose to use index to represent value
        # and use adding a number to current position 
        # to represent existing/non-existing value
        #   1) for example nums[i] += (n+1) means value (i+1) exists
        #   2) values not in [1 : n] are not useful and we can just
        #      change them to be 0 to represent non-existing
        #      and we do nothing on nums
        n = len(nums)
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 0
        # for example: nums = [3,4,-1,1]               
        # after this loop: nums = [3,4,0,1], meaning:
        # we have 3 values: 3, 4, 1 that we care
        # we don't care about 0
        
        # Then we go through nums again, if nums[i] = x is in the range of 
        # [1 : n] (we care), we use index (x - 1) to record that we have
        # seen x by adding n + 1 to nums[x - 1]
        for i in range(n):
            if 1 <= nums[i] % (n + 1) <= n: # if we care about this value, we add (n+1) to it
                index = nums[i] % (n + 1) - 1 # we use mod to find index because:
                nums[index] += n + 1 # nums[index] could += (n+1) multiple times
        # for 3: nums[2] += 5
        # for 4: nums[3] += 5
        # for 0: nothing
        # for 1: nums[0] += 5
        # [8, 4, 5, 6], meaning:
        # value 1: 8 >= 5: it exists in original nums
        # value 2: 4 < 5: it doesn't exist
        # value 3: 5 >= 5: exists
        # value 4: 6 >= 5: exists
        # value 5: None: if all 1 to 4 exist, 5 doesn't exist
        
        # Finally we just need to find the first index i for which 
        # nums[i] is less than n + 1 (which means we never met number
        # i + 1 so we did not add n + 1 to nums[i])
        for i in range(n):
            if nums[i] <= n:
                return i + 1
        
        return n + 1