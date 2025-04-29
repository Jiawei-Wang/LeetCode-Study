# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total = 0
        def subtree_sum(node):
            nonlocal total
            left_sum = 0
            right_sum = 0
            if not node:
                return (0, 0)
            if node.left:
                left_sum = node.left.val + sum(subtree_sum(node.left))
            if node.right:
                right_sum = node.right.val + sum(subtree_sum(node.right))
            total += abs(left_sum - right_sum)
            return (left_sum, right_sum)

        subtree_sum(root)
        return total


            
        
        
