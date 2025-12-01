# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. find path from root to s and root to d
# 2. remove common prefix path
# 3. replace all steps from root to s with U
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(node: TreeNode, val: int, path: List[str]) -> bool:
            if node.val == val:
                return True
            if node.left and find(node.left, val, path):
                path += "L"
            elif node.right and find(node.right, val, path):
                path += "R"
            return path

        s, d = [], []
        find(root, startValue, s)
        find(root, destValue, d)
        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        return "".join("U" * len(s)) + "".join(reversed(d))