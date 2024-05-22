# 2024
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        def dfs(node):
            if not node:
                return
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            answer.append(node.val)
        dfs(root)
        return answer