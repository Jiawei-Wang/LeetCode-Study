"""
Initial thoughs: 
1. first we construct the tree:
    range is [1, n] (included), pick mid as root
    then build left subtree and right subtree recursively
    each time pick mid of current value range as node value
2. now we have a tree with many different paths from root to leaf
3. DFS from root, get sum of all paths, pick the one with biggest sum

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def constructTree(self, start, end):
        if start > end:
            return None
        
        mid = (start + end) // 2
        root = TreeNode(mid)
        
        root.left = self.constructTree(start, mid - 1)
        root.right = self.constructTree(mid + 1, end)
        
        return root

    def maxPathSum(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        
        left_sum = self.maxPathSum(root.left)
        right_sum = self.maxPathSum(root.right)
        
        return root.val + max(left_sum, right_sum)

    def getMoneyAmount(self, n: int) -> int:
        root = self.constructTree(1, n)
        return self.maxPathSum(root)

for example: n = 10
using the method above, we have this tree:
                 5                   <- root
        2                 8          <- second level
     1     3          6       9      <- third level
              4         7        10  <- leaf level

and getMoneyAmount will return 22: 
    which is the maximum path in this tree 5+8+9
meaning guarantee a win regardless target number will cost 22: 
    amount of money to pay is maximum when target = 10

This answer is incorrect because the question asks: 
what is the minimum amount of money to pay to guess any number
which means we need to find the minimum value of (all maximum paths in all possible trees)
and the above answer only builds 1 tree, and we only have the value of maximum path in this tree

the best tree for n = 10 is actually:
                 7                   <- root
        3                 9          <- second level
    1       5         8       10     <- third level
      2   4   6                      <- leaf level
and the maximum path is: 7+9 = 16
meaning to guarantee a win, we at most spend 16: guess 7 first, then guess 9, then 10 is target

now the question becomes: how do we build the best tree 
1. there is an optimal value for root (same for all other nodes as well), but we don't know the value
2. regardless of the root value (5 or 7 or something else), we have to handle the worst case within the 2 subtrees
3. so if both subtrees are equal, or have minimum differences, the worse case is mitigated
4. which means if we have an optimal way to build tree for a smaller range, we can use it for bigger range
5. get rid of the tree: if we know the min cost for a smaller range, we can use it for bigger range
6. so we use dp:
    1) base case: min cost to guess in range <= 1 is 0 (equal to the leaf node in the above tree answer)
    2) for range >= 2: min cost to guess this range is (the longest path on the best tree)
    3) we don't know which number is root for best tree, so we try everyone in the range
    4) relation between problem and subproblem: min cost = min of all (guess value + max(left subrange, right subrange))
"""
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)] # dp[i][j]: min cost to guess in [i, j] (included)
        
        def dfs(start, end):
            # if the range is invalid or only one number is left
            if start >= end:
                return 0 
                # for example dp[5][5] = 0: if 5 is the only number left, it costs 0 to guess
                # for example dp[5][4] = 0: nothing to guess in [5, 4]
            
            # if the result is already calculated, return it
            if dp[start][end] != 0:
                return dp[start][end]
            
            # now to find out min cost for [start, end]
            min_cost = float('inf')
            for guess in range(start, end + 1): # we don't know which number to choose, so just choose everyone
                cost = guess + max(dfs(start, guess - 1), dfs(guess + 1, end))
                min_cost = min(min_cost, cost)
            dp[start][end] = min_cost

            return min_cost
        
        return dfs(1, n)






