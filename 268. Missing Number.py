# brute force: nlogn
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if nums[0]:
            return 0
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 2:
                return nums[i]-1
        return nums[-1]+1


# n
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
        start = 0
        for i in range(len(nums)):
            start = start ^ i ^ nums[i]
        i += 1
        return start ^ i
    
"""
从n个元素中找到缺失的那一个，例：
[3,0,2]: 缺少1
len(nums) = 3, index = [0,1,2]
所以for循环中是：start = 0 ^ (0^1^2) ^ (0^2^3)
如果把它看成是4次循环而不是3次，则可以理解最后结尾时有一个index没有对应值，它就是答案
所以 ^ len(nums)+1 可以得到该值
"""


# 2024
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        xor = 0
        for i in range(length):
            xor ^= i
            xor ^= nums[i]
        xor ^= length
        return xor

