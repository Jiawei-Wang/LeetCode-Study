# input: unsorted list of integers
# output: length of longest subsequence (not subarray) of the list


# solution 1：decision tree
# time 2^n
# for every element, add it or don't add it, pick the longest answer
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def find_LIS_length(prev, cur_pos):
            # for a position, we have 3 options:

            # if it is out of bound, return 0
            if cur_pos == len(nums):
                return 0

            # if it is bigger than prev, we can take it or not take it
            taken = 0
            if nums[cur_pos] > prev:
                # if we take it, it becomes the new prev
                taken = 1 + find_LIS_length(nums[cur_pos], cur_pos + 1)
            
            # regardless of its value compared to prev, we can always not take it
            not_taken = find_LIS_length(prev, cur_pos + 1)

            return max(taken, not_taken)

        return find_LIS_length(float('-inf'), 0)


# solution 2: DP, same DFS as decision tree but with cache
# time n^2 space n 
# Top down: 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums) # base case: LIS from this position is only itself
        for i in range(len(nums) - 1, -1, -1):
            # for LIS[4]: its max value is max(1, LIS[5], LIS[6], LIS[7], etc)
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)

# bottom up dp
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)


# solution 3: patient sorting by using binary search
# nlogn
# 核心逻辑：tails：array storing the smallest tail of all increasing subsequences with length i+1 in tails[i]
# 举例：在[3,6,5,7]中长度为2的所有subsequence中（共有5个(36,35,37,67,57)）末尾元素最小的为[3,5]，所以tail[1] = 5
# 观察：长度为3的所有subsequence中最小的一定大于5
# (if we can find a length = 3 subsequence with tail < 5, then the length = 2 subsequence inside this 
#  length = 3 subsequence has tail smaller than 5)
# 所以整个tail是个递增list (tail[n] > tail[n-1])
# so we can add elements into tail list by using binary search
# for an element x: 
# (1) if x is larger than all elements in tail, which means x cannot update any of all current best subsequences
#     we append it to tail, increase the size by 1
# (2) if tails[i-1] < x <= tails[i], update tails[i]
#      why we don't need to update all following elements behind tails[i]:
#      for example: [3, 6, 7, 5]
#      till 7, we have tails = [3, 6, 7]
#      when we get 5, we go through binary search, update tails[1] = 5 
#      which means length = 2 subsequence has a smaller tail now
#      but length = 3 subsequence remains the same, still [3, 6, 7]
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums) # tail[5] = 4: for all subsequences of length 6, smallest tail element is 4
        size = 0 # 初始LIS长度为0

        for x in nums:
            # first loop: tails[0] = nums[0], size = 1
            # all other loops:
            # 1. we find location of x
            # 2. we either append x to the end (x is too big for any current tail)
            #    or update a current value to x (x can replace a current tail and make it smaller)
            # 3. keep updating tail list length
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

        