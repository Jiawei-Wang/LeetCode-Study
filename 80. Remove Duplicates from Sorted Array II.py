# basic logic: 
# we move on the input array from left to right, every time we find a new value, 
# we assign old value to the left side of the array

# two pointers
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0 # left is where we assign value in place
        right = 0 # right is the value we are visiting

        # every loop we find all occurrences of the new value
        # and assign at most 2 to the left part of list
        while right < len(nums):
            
            target = nums[right]
            count = 1
            while right < len(nums)-1 and nums[right+1] == target:
                count += 1
                right += 1
            
            for j in range(min(2, count)):
                nums[left] = target
                left += 1
            
            right += 1
        
        return left


# one pointer
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 # i is where we assign value in place
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i

        # for the first two elements, we keep them
        # for the rest of the elements, if element has occured more than twice, we don't do anything
        # if element has occured <= twice, we assign and move forward with index i