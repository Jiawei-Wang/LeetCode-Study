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


# for every element, we can: choose to include it, or not include it
# for n elements, we have 2^n combinations
# so this becomes a decision tree: every time we go to the leaf, append the leaf to answer
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            # when we get to leaf node, append current array to answer array
            if i >= len(nums): 
                ans.append(subset.copy())
                return
            # for a node, we can add it or not add it
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
        
        ans = []
        subset = [] # we only need one variable because we constantly remove element from it when we leave current loop
        dfs(0)
        return ans

"""
use [1,2,3] as example to understand execution:
1. subset = [1], go into next loop
2. subset = [1,2], go into next loop
3. subset = [1,2,3], go into next loop
4. ans.append([1,2,3]), go back to last loop
5. subset = [1,2], go into next loop
6. ans.append([1,2]), go back to last loop
7. etc
final output is: 
[[1,2,3],[1,2],[1,3],[1],[2,3],[2],[3],[]]
"""