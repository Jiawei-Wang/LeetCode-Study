# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# traversal first + merge later
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        # in order traversal 
        def inorder(root, arr):
            if not root:
                return
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)

        a, b = [], []
        inorder(root1, a)
        inorder(root2, b)

        # merge two sorted lists
        res = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1

        res.extend(a[i:])
        res.extend(b[j:])
        return res


# traversal while merging
class Solution:
    def getAllElements(self, root1, root2):
        def push_left(node, stack):
            while node:
                stack.append(node)
                node = node.left

        s1, s2 = [], []
        push_left(root1, s1)
        push_left(root2, s2)

        res = []
        while s1 or s2:
            # choose which stack has smaller next value
            if not s2 or (s1 and s1[-1].val <= s2[-1].val):
                node = s1.pop()
                res.append(node.val)
                push_left(node.right, s1)
            else:
                node = s2.pop()
                res.append(node.val)
                push_left(node.right, s2)

        return res
