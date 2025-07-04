"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        answer = []
        def dfs(node):
            if not node:
                return
            if node:
                answer.append(node.val)
            if node.children:
                for child in node.children:
                    dfs(child)
        
        dfs(root)
        return answer
        