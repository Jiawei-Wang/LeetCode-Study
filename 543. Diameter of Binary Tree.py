# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 从root出发的两条并不一定是最长线路，需要找到每个从每个点出发的线路长度并保留最大值

        self.res = 0

        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)

            # 对于一个点，其res为res或左右子树长度之和
            self.res = max(self.res, left+right)

            # 对于一个点而言，只需要保留其较长的那个子树并 +1
            return 1 + max(left, right)

        depth(root)
        return self.res
