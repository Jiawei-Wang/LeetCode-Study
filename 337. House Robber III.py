# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# just going down the tree without DP
# 1. if node is picked, skip child nodes and go for grandchild nodes
# 2. if node is not picked, go for child nodes
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        money = 0
        if root.left:
            money += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            money += self.rob(root.right.left) + self.rob(root.right.right)
        
        return max(root.val + money, self.rob(root.left) + self.rob(root.right))


# DP
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dp(root, hashmap):
            if not root:
                return 0
            if root in hashmap:
                return hashmap.get(root) # use existing result instead of calculating again
            money = 0
            if root.left:
                money += dp(root.left.left, hashmap) + dp(root.left.right, hashmap)
            if root.right:
                money += dp(root.right.left, hashmap) + dp(root.right.right, hashmap)
            money = max(money + root.val, dp(root.left, hashmap) + dp(root.right, hashmap))
            hashmap[root] = money # put calculated result into hashmap
            return money

        hashmap = dict() # node, integer
        return dp(root, hashmap)


# better DP: 
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def betterDP(root):
            if not root:
                return [0, 0]
            left = betterDP(root.left)
            right = betterDP(root.right)
            res = [0, 0]
            res[0] = max(left[0], left[1]) + max(right[0], right[1]) 
            res[1] = root.val + left[0] + right[0]
            return res
        res = betterDP(root)
        return max(res[0], res[1])

        