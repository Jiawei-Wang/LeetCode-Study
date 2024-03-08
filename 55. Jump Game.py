# 读题想法：需要关心的唯一问题就是可不可以跨过所有的 '0'


# brute-force backjumping: try every single jump pattern
# 答案这样理解：
# canjumpFromPosition检查是否可以从一个position跳到末尾
# 如果已经是末尾则返回true，如果不是的话，找出从这个点能跳的范围
# 因为0不能跳，所以就返回了上一层，重新寻找一个新点
class Solution:
    def canjumpFromPosition(self, position, nums):
        if position == len(nums) - 1:
            return True

        furthestJump = min(position+nums[position], len(nums)-1)
        for nextPosition in range(position+1, furthestJump+1):
            if self.canjumpFromPosition(nextPosition, nums):
                return True

        return False

    def canJump(self, nums: List[int]) -> bool:
        return self.canjumpFromPosition(0, nums)
# Time: O(2^n), 超时


# improved backjumping: try to make biggest jump first
class Solution:
    def canjumpFromPosition(self, position, nums):
        if position == len(nums) - 1:
            return True

        furthestJump = min(position+nums[position], len(nums)-1)
        for nextPosition in reversed(range(position+1, furthestJump+1)):
            if self.canjumpFromPosition(nextPosition, nums):
                return True

        return False

    def canJump(self, nums: List[int]) -> bool:
        return self.canjumpFromPosition(0, nums)
# Time: O(2^n), 超时


# DP top-down:
# 理解如下：初始化只能到达0，然后从i=0开始遍历，找到从每个点出发最远能到达的位置，如果当前点本身并不能被到达，返回false
# 所以在进入新一轮循环（即遍历到下一个点时），先检查从前面的点到它能否到达，如果能，则继续从它找到后续能到达的最远点
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach: # 没有任何前面的点能到达这个点
                return False
            maxReach = max(maxReach, i+nums[i]) # 这个点可被到达，那么更新后续最远可到达点
        return True
# Time: O(n^2)


# DP bottom-up:
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = [-1 for i in range(len(nums))]
        m[len(nums)-1] = True # 初始化设末尾点为目标

        last = len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= last: # 如果当前的点可以到达目标，则设为True
                m[i] = True
                last = i # 将当前的点设为新的目标
                continue
            m[i] = False # 如果当前的点到达不了目标则设为False

        return m[0] # 对于出发点而言，如果它范围内所有的目标都为False，则它也为False
# Time: O(n^2)


# Greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j = 0
        for i, x in enumerate(nums): 
            if j < i: return False
            j = max(j, i+x)
        return True
# Time: O(n)



# 03-07-2024
# bottom up dp: O(n^2)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums.reverse()
        length = len(nums)
        dp = [True] + [False] * (length - 1)
        
        for index in range(1, length): # for every jump point
            coverage = nums[index] 
            # we just need find one True within the range
            for i in range(index, index-coverage-1, -1):
                if i >= 0 and dp[i] == True:
                    dp[index] = True
                    break
        return dp[-1]

# move goal towards starting point, greedy: O(n)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        goal = length - 1 # current goal is the last element
        for index in range(length-1, -1, -1): # for every index (backwards)
            if index + nums[index] >= goal: # if we can jump from index to goal
                goal = index # then index becomes the new goal
        
        return goal == 0

        