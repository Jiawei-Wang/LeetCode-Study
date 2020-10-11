# 读题想法: 1.排序, 2.不排序

# 解法1: 排序
# NlogN
"""
要考虑的corner case如下:
1. 空list
2. 从头至尾都是连续的list: [0, 1, 2]
3. 中间有重复元素的list: [0, 1, 1, 2]
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        
        nums.sort()
        ans = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
            elif nums[i] == nums[i-1]:
                pass
            else:
                ans = max(count, ans)
                count = 1
        ans = max(count, ans)
        return ans