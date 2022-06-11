# 难点：找到递增subsequence而不是subarray

# 暴力解：decision tree：对每个元素，选择加入或者不加入，最后所有可能解中找到符合条件且最长的 time 2^n

# DFS with cache： 如果我们能找到从index=5开始的LIS，那么我们就能找到从index=4开始的LIS
# 转化为top down dp: dp[i]代表index=i处能获得的最长LIS，那么dp[i] = max(1, dp[i+1] if nums[i] < nums[i+1], dp[i+2] if nums[i] < nums[i+2], etc)
# time n^2 space n
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums) # 初始化最长都为1
        # bottom up dp
        for i in range(len(nums) - 1, -1, -1):
            # 对于LIS[4]而言，它的最大值是max(1, LIS[5], LIS[6], LIS[7], etc) （它自身，或者后面所有比它大的元素对应的LIS中的最大者）
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)


# patient sorting: nlogn
# 核心逻辑：tails：array storing the smallest tail of all increasing subsequences with length i+1 in tails[i]
# 举例：在[3,6,5,7]中长度为2的所有subsequence中（共有5个(36,35,37,67,57)）末尾元素最小的的为[3,5]，所以tail[1] = 5
# 观察：长度为3的所有subsequence中最小的一定大于tail[1]，所以整个tail是个递增list，可以使用binary search
# (1) if x is larger than all tails, append it, increase the size by 1
# (2) if tails[i-1] < x <= tails[i], update tails[i]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0 # 初始LIS长度为0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size