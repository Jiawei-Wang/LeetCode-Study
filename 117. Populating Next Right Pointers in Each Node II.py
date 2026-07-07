"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        current_level = [root]

        while current_level:
            next_level = []
            length = len(current_level)

            for i in range(length-1):
                node = current_level[i]
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

                node.next = current_level[i+1]

            node = current_level[-1]
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            node.next = None
        
            current_level = next_level
        
        return root
                

