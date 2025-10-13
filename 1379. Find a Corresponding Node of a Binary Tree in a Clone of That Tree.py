# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(origin, clone):
            if not origin:
                return None

            if origin == target:
                return clone

            left = dfs(origin.left, clone.left)
            if left:
                return left

            right = dfs(origin.right, clone.right)
            if right:
                return right

        return dfs(original, cloned)


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [(original, cloned)]
        while stack:
            origin, clone = stack.pop()
            if origin == target:
                return clone
            if origin.right:
                stack.append((origin.right, clone.right))
            if origin.left:
                stack.append((origin.left, clone.left))
