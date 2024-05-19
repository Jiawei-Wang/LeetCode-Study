# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# solution 1: turn tree into 1d sorted list
# 思路：BST中每个元素的位置均固定，所以DFS就可以找到第K个元素
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            if not node:
                return []
            else:
                return inorder(node.left) + [node.val] + inorder(node.right)

        return inorder(root)[k - 1]


# solution 2: dfs directly
class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        self.res = None
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        self.helper(node.left) 
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)


# solution 3: dfs with stack
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
