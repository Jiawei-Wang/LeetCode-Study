# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0

        def travel(node):
            nonlocal total 
            
            if not node:
                return
            
            if node.right:
                travel(node.right)
            
            total += node.val
            node.val = total

            if node.left:
                travel(node.left)
        
        travel(root)
        return root