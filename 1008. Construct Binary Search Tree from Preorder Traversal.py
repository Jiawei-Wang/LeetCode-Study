# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # Binary search

        # n^2
        if not preorder:
            return None

        # 用地一个元素建造root node
        root = TreeNode(preorder[0])

        # bisect参考：https://docs.python.org/zh-cn/3.6/library/bisect.html
        # i是root在preorder中本应存在位置，左边均比其小，右边均比其大
        i = bisect.bisect(preorder, preorder[0])

        # 将在preorder中位于i之前的作为root的左子树进行recursion，右子树同理
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])

        return root

        # Time: 62%
        # Space: 6%


        # nlogn
        # 与前一个答案同理，使用bisect找到root的index然后将list前后部分分别建成左右子树
        def helper(i, j):
            if i == j:
                return None
            root = TreeNode(preorder[i])
            mid = bisect.bisect(preorder, preorder[i], i + 1, j)
            root.left = helper(i + 1, mid)
            root.right = helper(mid, j)
            return root

        return helper(0, len(preorder))

        # Time: 62%
        # Space: 6%

class Solution:
    i = 0
    # 与上一种解法相比多使用一个bound参数
    def bstFromPreorder(self, A, bound=float('inf')):

        if self.i == len(A) or A[self.i] > bound:
            return None
        root = TreeNode(A[self.i])
        self.i += 1
        root.left = self.bstFromPreorder(A, root.val)
        root.right = self.bstFromPreorder(A, bound)
        return root

    # Time: 96%
    # Space: 6%
