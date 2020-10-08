# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursion
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.preorder(root,ans)
        return ans
    def preorder(self,root,ans):
        if not root:
            return
        ans.append(root.val)
        self.preorder(root.left,ans)
        self.preorder(root.right,ans)


# iteration
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        while root or stack:
            if root:
                ans.append(root.val)
                if root.right:
                    stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()
        return ans
