# library
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 读题第一想法：python有没有直接进行排列组合的function
        # 答案：itertools.permutations
        return list(itertools.permutations(nums))

#
