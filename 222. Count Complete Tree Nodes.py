# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        counter = 0
        if not root:
            return counter
        bfs = deque()
        bfs.append(root)
        while bfs:
            currentNode = bfs.popleft()
            counter += 1
            if currentNode.left:
                bfs.append(currentNode.left)
            if currentNode.right:
                bfs.append(currentNode.right)
        return counter


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        compare the depth between left sub tree and right sub tree.
        A, If it is equal, it means the left sub tree is a full binary tree (last leaf is on right sub tree, both have same depth)
        B, It it is not , it means the right sub tree is a full binary tree (last leaf is on left sub tree, left sub tree is one level deeper)
        """
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)