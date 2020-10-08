# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 思路：BST中每个元素的位置均固定，所以DFS就可以找到第K个元素
        def inorder(r):
            # 将每个元素的值放进一个list中
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        return inorder(root)[k - 1]
