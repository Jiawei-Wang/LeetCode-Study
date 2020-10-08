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
# 理解如下：初始化只能到达0，然后循环找到从每个点出发最远能到达的位置，如果当前点本身并不能被到达，返回false
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i in range(len(nums)):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i+nums[i])
        return True
# Time: O(n^2)


# DP bottom-up:
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = [-1 for i in range(len(nums))]
        m[len(nums)-1] = True

        last = len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= last:
                m[i] = True
                last = i
                continue
            m[i] = False

        return m[0]
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
