# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def is_valid(array, level):
            # odd indexed level: all nodes are even integers and strictly decreasing
            if level % 2:
                current = float("inf") 
                for node in array:
                    value = node.val
                    if value % 2 or value >= current:
                        return False
                    current = value
                return True
            else:
                current = -float("inf")
                for node in array:
                    value = node.val
                    if value % 2 == 0 or value <= current:
                        return False
                    current = value
                return True
        
        level = 0
        queue = [root]

        while queue:
            if not is_valid(queue, level):
                return False

            next_queue = []
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
            level += 1
        
        return True
