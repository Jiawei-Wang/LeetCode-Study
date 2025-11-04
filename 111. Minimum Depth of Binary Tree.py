# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            # we know at least one leg exists
            #   if both exist, just pick the shortest one
            #   if only one exists
            # set the empty leg to float("inf")
            left = 1 + self.minDepth(root.left) if root.left else float("inf")
            right = 1 + self.minDepth(root.right) if root.right else float("inf")
            return min(left, right) # so return value will always be the one that exists
        
        