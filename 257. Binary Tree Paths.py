# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def dfs(node, path):
            if node and not node.left and not node.right:
                paths.append(path + [node.val])
                return
            
            if node.left:
                dfs(node.left, path + [node.val])
            if node.right:
                dfs(node.right, path + [node.val])

        dfs(root, [])
        answer = []
        for path in paths:
            path_string = '->'.join(map(str, path))
            answer.append(path_string)
        return answer



        