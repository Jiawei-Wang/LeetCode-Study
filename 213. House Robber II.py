# two loops: rob first house and not rob first house
# rob first house = not rob last house
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # first loop
        left = 0
        right = 0 # we only need two variables since we don't care about house[1] anymore once we reach house[4]
        for i in range(len(nums)-1):
            tmp = left
            left = max(right+nums[i], left) # same as House Robber 1: dp[i] = max(dp[i-2]+nums[i], dp[i-1]) 
            right = tmp
        
        # second loop
        left2 = 0
        right2 = 0
        for i in range(1, len(nums)):
            tmp = left2
            left2 = max(right2+nums[i], left2)
            right2 = tmp
        
        return max(left, left2)


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # pick 0-th and skip last one 
        first = 0
        second = nums[0]
        for i in range(1, len(nums)-1):
            first, second = second, max(second, first + nums[i])
        answer1 = second

        # pick last one and skip 0-th
        first = 0
        second = nums[1]
        for i in range(2, len(nums)):
            first, second = second, max(second, first + nums[i])
        answer2 = second

        return max(answer1, answer2)