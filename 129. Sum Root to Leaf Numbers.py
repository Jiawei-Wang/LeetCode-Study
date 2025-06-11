# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(node, cur_sum):
            nonlocal total
            if not node.left and not node.right:
                total += (cur_sum * 10 + node.val)
                return
            
            if node.left:
                dfs(node.left, cur_sum*10+node.val)
            if node.right:
                dfs(node.right, cur_sum*10+node.val)

        dfs(root, 0)
        return total