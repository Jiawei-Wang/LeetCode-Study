# library
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 读题第一想法：python有没有直接进行排列组合的function
        # 答案：itertools.permutations
        return list(itertools.permutations(nums))


# DFS on decision tree
class Solution:
    def permute(self, nums):
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        # 如果遍历完了就将答案写入
        if not nums:
            res.append(path) # 并不需要return，因为此method是对res进行修改
        
        # 如果还没遍历完就进入下一层dfs
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)    

            
# 递归
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 已经到达最底层，返回唯一一个数字
        if len(nums) <= 1:
            return [nums]

        ans = []
        # 在这一层，对于剩余的每个可选数字：
        for i, num in enumerate(nums):

            # 选择一个，将它排除在下一层的选择之外
            n = nums[:i]+nums[i+1:]

            # 对于下一层返回的所有可能排列组合，头部都加上num
            for y in self.permute(n):
                ans.append([num]+y)  # 使用 [num]+y 把num加到y这个list的头部

        return ans  # 返回这一层的答案给上一层
