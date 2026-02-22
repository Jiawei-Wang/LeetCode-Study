# we have n unique numbers in the range [0, n]
# which means there is one missing number 
# find that missing number
# for example: [9,6,4,2,3,5,7,0,1]
# in total 9 numbers between [0, 9]
# and the missing one is 8


# brute force: nlogn
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for index, number in enumerate(nums):
            if index != number:
                return index
        return len(nums) # in case the missing number is n


# using a set: n
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = set(i for i in range(len(nums)+1))
        for i in nums:
            ans.remove(i)
        return ans.pop()


# math
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n+1)*n//2 - sum(nums)


# XOR: time n space 1
# any number ^ itself = 0 
# any number ^ 0 = itself
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        for i in range(n):
            xor ^= i
            xor ^= nums[i]
        # for example [3, 0, 1]
        # index = [0, 1, 2]
        # so 0 matches 0, 1 matches 1, index 2 and value 3 don't match
        # so we just need to ^= 3 to get 2 
        xor ^= n
        return xor

