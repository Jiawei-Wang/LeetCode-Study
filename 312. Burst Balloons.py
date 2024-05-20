"""
decision tree: each time pick one ballon, O(n!) paths
find redundancy: use cache with decision tree
observation: maxCoins for remaining balloons doesn't depend on already bursted balloons, so DP is possible
dp difficulity: sub problem is hard to define by picking the first balloon to burst
                because left subarray and right subarray merge
dp optimization: picking last balloon to burst each time instead
                 because in this way the newly formed array is fixed
"""

# dp[i][j]: coins obtained from bursting all the balloons between index i and j (not including i or j)
# becasue we add imaginary balloon on each side, final answer is dp[0][n - 1] 
# we let x be the index of the last balloon to burst in range (i, j)
# the coins we get from this burst is nums[i] * nums[x] * nums[j]
# so dp[i][j] = max(dp[i][x] + nums[i] * nums[x] * nums[j] + dp[x][j]) for all possible x)
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        # k+1: how many balloons we have 
        # since we have two imaginary balloons, we start from k=2 
        # meaning we have 2+1=3 balloons (including two imaginary ones)
        for k in range(2, n): 
            # pick all possible ranges
            for left in range(0, n - k):
                right = left + k
                # for this range, pick all possible balloons
                for i in range(left + 1,right):
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        
        # we don't need base case because smallest k is 2
        # so first loop left = 0, right = 2, i can only be 1
        # we have one balloon and dp[0][2] with dp[0][1] == dp[1][2] == 0
        # actually because right - left >= 2, we will never calculate dp[1][2] or dp[3][4] or etc

        return dp[0][n - 1]    