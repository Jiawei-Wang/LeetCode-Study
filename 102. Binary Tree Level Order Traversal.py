from collections import deque

# BFS + queue: 把一层遍历完，然后遍历下一层（这层所有node的左右子node）
class Solution:
    def levelOrder(self, root):
        if not root: 
            return []        
        queue = deque([root])
        res = []
        
        while queue:
            cur_level = []
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur_level.append(node.val)
            res.append(cur_level)
        return res