# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # DFS Recursively
    def hasPathSum(self, root, sum):
        res = []
        self.dfs(root, sum, res)
        # any()：检查res中是否有至少一个True
        return any(res)

    def dfs(self, root, target, res):
        if root:
            # 如果leaf node和剩下的值相等，添加一个True
            if not root.left and not root.right:
                if root.val == target:
                    res.append(True)
                else:
                    res.append(False)
            if root.left:
                self.dfs(root.left, target-root.val, res)
            if root.right:
                self.dfs(root.right, target-root.val, res)


    # DFS with stack
    def hasPathSum2(self, root, sum):
        if not root:
            return False
        # stack存储的是每个node和到它为止所有node的和
        stack = [(root, root.val)]
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right:
                if val == sum:
                    return True
            if curr.right:
                stack.append((curr.right, val+curr.right.val))
            if curr.left:
                stack.append((curr.left, val+curr.left.val))
        return False


    # BFS with queue
    def hasPathSum3(self, root, sum):
        if not root:
            return False
        queue = [(root, sum-root.val)]
        while queue:
            curr, val = queue.pop(0)
            if not curr.left and not curr.right:
                if val == 0:
                    return True
            if curr.left:
                queue.append((curr.left, val-curr.left.val))
            if curr.right:
                queue.append((curr.right, val-curr.right.val))
        return False
