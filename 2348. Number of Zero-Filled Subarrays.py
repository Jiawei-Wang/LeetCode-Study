# one 0   : 1
# two 0s  : 2 + 1 = 3
# three 0s: 3 + 2 + 1 = 6
# n 0s    : n + (n-1) + (n-2) + ... + 1 = n(n+1)/2
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        j = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                j = i + 1 # j will be anchored to the first 0 
            res += i - j + 1
        return res