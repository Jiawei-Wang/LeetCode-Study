"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        bfs = deque()
        bfs.append(root)

        while bfs:
            level_size = len(bfs)
            for i in range(level_size):
                current_node = bfs.popleft()
                if i < level_size - 1: # if not the right most node
                    current_node.next = bfs[0]
                if current_node.left: 
                    bfs.append(current_node.left)
                if current_node.right:
                    bfs.append(current_node.right)
        
        return root

