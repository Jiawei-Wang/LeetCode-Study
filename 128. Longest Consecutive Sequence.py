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


# 解法2: HashSet and Intelligent Sequence Building
# N
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # list to set: O(n)
        num_set = set(nums)

        longest_streak = 0
        for num in num_set:
            # Query a set: O(1)
            if num - 1 not in num_set: # if num is the start of a new streak
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


# 05-01-2022回顾
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # time n^2 space n 
        # if not nums:
        #     return 0
        # max_ans = 1
        # nums = set(nums)
        # for i in nums:
        #     ans = 1
        #     i += 1
        #     while i in nums:
        #         ans += 1
        #         i += 1
        #     max_ans = max(max_ans, ans)
        # return max_ans
        
        # 对上面解法的优化
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums: # 只检查每个streak的头部，大大缩短了时间
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best