# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
For example: [1, 2, 3, 4, 5]
                1
        2               3
    4       5
"""
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


# 1. DFS Preorder: 
#     1) Node -> Left -> Right
#     2) execution: [root.val] + preorder(root.left) + preorder(root.right) if root else []
#     3) output: [1,2,4,5,3]
def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []



# 2. DFS Inorder:
#     1) Left -> Node -> Right
#     2) execution: inorder(root.left) + [root.val] + inorder(root.right) if root else []
#     3) output: [4,2,5,1,3]
def inorder(root):  
    return  inorder(root.left) + [root.val] + inorder(root.right) if root else []


# 3. DFS Postorder:
#     1) Left -> Node -> Right
#     2) execution: postorder(root.left) + postorder(root.right) + [root.val] if root else []
#     3) output: [4,5,2,3,1]
def postorder(root):
    return  postorder(root.left) + postorder(root.right) + [root.val] if root else []


# 4. BFS:
#     1) Node -> Left -> Right
#     2) execution: iteration with queue
#     3) output: [1,2,3,4,5]
from collections import deque
def bfs(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
    
    
print(preorder(root))
print(inorder(root))
print(postorder(root))
print(bfs(root))
