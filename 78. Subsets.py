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