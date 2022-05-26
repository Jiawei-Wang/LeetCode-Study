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


