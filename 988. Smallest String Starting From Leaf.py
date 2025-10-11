# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def transform(path):
            array = [chr(ord('a') + val) for val in path]
            return "".join(array[::-1])

        answer = []

        def dfs(node, path):
            if not node.left and not node.right:
                answer.append(transform(path+[node.val]))
                return
            if node.left:
                dfs(node.left, path+[node.val])
            if node.right:
                dfs(node.right, path+[node.val])
        
        dfs(root, [])

        return min(answer)