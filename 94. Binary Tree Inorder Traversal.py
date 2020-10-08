# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# recurstion
class Solution:
    # inorder：左中右
    # 对于每一个node而言，返回顺序是它的左子树，自身，右子树
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.helper(root, ans)
        return ans

    def helper(self,root,ans):
        if root:
            if root.left:
                self.helper(root.left,ans)
            ans.append(root.val)
            if root.right:
                self.helper(root.right,ans)


# iteration
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
