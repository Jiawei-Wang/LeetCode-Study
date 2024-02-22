# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # O(n) BFS
        array = []
        pending = deque()
        pending.append(root)
        while pending:
            current = pending.popleft()
            array.append(current.val)
            if current.left:
                pending.append(current.left)
            if current.right:
                pending.append(current.right)
        
        # O(nlogn) build a sorted array
        sortedArray = sorted(array)

        # O(n) get answer
        minimum = float("inf")
        for i in range(len(sortedArray)-1):
            minimum = min(minimum, sortedArray[i+1] - sortedArray[i])
        return minimum


# inorder traversal DFS
class Solution(object):
    pre = -float('inf') # the ghost leaf that is on the left side of the left most leaf
    res = float('inf') 

    def minDiffInBST(self, root):
        if root.left:
            self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val # set pre to current node val
        if root.right:
            self.minDiffInBST(root.right)
        return self.res