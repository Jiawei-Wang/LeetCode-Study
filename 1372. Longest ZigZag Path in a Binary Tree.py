# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxStep = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, True, 0)
        self.dfs(root, False, 0)
        return self.maxStep

    def dfs(self, node: TreeNode, isLeft: bool, step: int):
        if node is None:
            return
        self.maxStep = max(self.maxStep, step)
        if isLeft:
            self.dfs(node.left, False, step + 1) # continue to left
            self.dfs(node.right, True, 1) # restart to right
        else:
            self.dfs(node.right, True, step + 1)
            self.dfs(node.left, False, 1)