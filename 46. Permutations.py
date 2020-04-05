# library
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 读题第一想法：python有没有直接进行排列组合的function
        # 答案：itertools.permutations
        return list(itertools.permutations(nums))


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
