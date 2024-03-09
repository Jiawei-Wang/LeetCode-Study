# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# recursion + DFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 将此node的左右子树指针对调
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invertTree(root.left) # DFS先检查左子树
        self.invertTree(root.right)
    
        return root


# interation + DFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 初始化stack
        stack = collections.deque()
        stack.append(root)
        
        while stack:
            node = stack.pop()
            tmp = node.left
            node.left = node.right
            node.right = tmp
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return root


# BFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            tmp = node.left
            node.left = node.right
            node.right = tmp
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        def switch(node):
            node.left, node.right = node.right, node.left
            if node.left:
                switch(node.left)
            if node.right:
                switch(node.right)
        
        switch(root)
        return root