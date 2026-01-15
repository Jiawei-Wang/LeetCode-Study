# important constraint: 1 <= nums[i] <= len(nums)
# every value is positive
# we have more indexes than values
# so we can just store occurrence of a value using the index
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0: # if x has appeared before 
                res.append(abs(x)) # add to output
            else: # if this is x's first appearance
                nums[abs(x)-1] *= -1 # mark the index as negative
        return res