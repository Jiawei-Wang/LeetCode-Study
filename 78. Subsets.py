# decision tree: 对于每个元素，有加入和不加入两种选择
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def helper(i, cur):
            if i == len(nums):
                ans.append(cur)
                return
            
            helper(i+1, cur+[nums[i]])
            helper(i+1, cur)
            
        helper(0, [])
        return ans


"""
2024
"""
# itertools
from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        length = len(nums)
        for k in range(length + 1):
            for combination in combinations(nums, k):
                subsets.append(combination)
        return subsets