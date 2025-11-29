# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        
        def dfs(node):
            nonlocal count 

            if not node.left and not node.right:
                count += 1
                return (node.val, 1) 
            
            left = right = (0, 0)
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            if node.val == (left[0] + right[0] + node.val) // (left[1] + right[1] + 1):
                count += 1

            return (left[0] + right[0] + node.val, left[1] + right[1] + 1)
        
        dfs(root)
        return count 