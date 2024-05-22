# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# inorder: left -> node -> right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        answer = float('inf')
        prev = TreeNode(float('-inf')) # dummy node on the left side of leftmost leaf node

        def dfs(node):
            nonlocal answer 
            nonlocal prev

            if not node:
                return

            dfs(node.left)
            answer = min(answer, node.val-prev.val)
            prev = node
            dfs(node.right)
        
        dfs(root)
        return answer 