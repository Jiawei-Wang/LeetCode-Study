# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]

        answer = 0
        while queue:
            answer = sum(node.val for node in queue)
            nxt = []
            for node in queue:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            queue = nxt
        return answer
