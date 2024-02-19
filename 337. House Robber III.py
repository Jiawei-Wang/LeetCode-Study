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
        