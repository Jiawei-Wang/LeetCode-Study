# 读题想法：题目要求从array中找出重复的元素以及缺失的元素

# 解法1：一次遍历，使用set寻找重复元素，使用另一个set寻找缺失元素
# Time n
# space 2n
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [-1,-1]
        duplicate = set()
        missing = set(n for n in range(1,len(nums)+1))

        for i in nums:
            if i in duplicate:
                ans[0] = i
            duplicate.add(i)

            missing.discard(i)
        ans[1] = missing.pop()
        return ans

            
