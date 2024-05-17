"""
How many unique ways can we build BST using 1 to n

1. every number can be used as root
2. so if we pick i as root, then left subtree is the same question for [1, i-1]
   right is for [i+1, n]
3. to do it using dp, we need a list dp[k]: number of unique BST for a sequence of length k (1 to k)
4. and a function F(i, n), 1 <= i <= n: number of unique BST where i is the root, with n as sequence length
5. so dp[n] = F(1, n) + F(2, n) + ... + F(n, n)
6. base case: dp[0] = dp[1] = 1
   there is only one combination to construct a BST out of a sequence of length 1 (only a root) or 0 (empty tree)
7. so for example F(3, 7): number of unique BST tree with 3 as root, and 7 as range
   we need to know the same question for [1, 2] and [4, 5, 6, 7]
   then F(3, 7) = dp[2] * dp[4]
   that is to say: F(i, n) = dp[i-1] * dp[n-i]
8 combine them together: dp[n] = dp[0] * dp[n-1] + dp[1] * dp[n-2] + ... + dp[n-1] * dp[0]
"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
        
