class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # 创建一个新的array
        ans = []
        # 记录当前sum的变量
        Sum = 0
        # 遍历nums
        for i in range(len(nums)):
            Sum += nums[i]
            ans.append(Sum)
        # 输出
        return ans
