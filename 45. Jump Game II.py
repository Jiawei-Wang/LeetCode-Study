class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0] + [float('inf')] * (length-1)
        for i in range(length):
            coverage = nums[i]
            for j in range(i+1, i+coverage+1):
                if j < length:
                    dp[j] = min(dp[i]+1, dp[j]) # find minimum steps to jump to j
        return dp[-1]


class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = 0 
        cur_end = 0
        cur_farthest = 0
        for i in range(len(nums)-1): # when we start from a position 
            cur_farthest = max(cur_farthest, i + nums[i]) # we first update the farthest position we can reach
            if i == cur_end: # we have reached the end of this jump
                jump += 1
                cur_end = cur_farthest # we find the range of next jump
        return jump
        
"""
example: for [2, 3, 0, 1, 4]
1. we start from 2, farthest will be index=2, 0-th jump reaches end, update end to 2, jump += 1
2. we move on to 3, farthest will be index=5
3. we move on to 0, farthest is still index=5, current jump reaches end, update end to 5, jump += 1
4. we move on to 1, farthest is still index=5
5. return jump value
"""