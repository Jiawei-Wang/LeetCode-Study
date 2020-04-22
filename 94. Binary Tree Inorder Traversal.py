# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # inorder：左中右

        # recursion
        # 对于每一个node而言，返回顺序是它的左子树，自身，右子树
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            if root.left:
                self.helper(root.left, res)
            res.append(root.val)
            if root.right:
                self.helper(root.right, res)


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # inorder：左中右

        # iterating method using Stack
        res = []
        stack = []
        curr = root
        while curr or stack:
            # 一直走到最左下角
            while curr:
                stack.append(curr)
                curr = curr.left
            # 逐个加入res中
            curr = stack.pop()
            res.append(curr.val)
            # 再把右边加进去
            curr = curr.right

        return res
