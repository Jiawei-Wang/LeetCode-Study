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


# 2024
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # on each level, number of nodes is unknown, and nodes don't always start from left to right
        # bfs w/ queue
        # we need to know which level we are on: two queues
        # time O(n), space O(n)

        # corner case
        if not root:
            return []
        
        current_level = deque()
        current_level.append(root)
        next_level = []
        answer = []
        current_answer = []

        while current_level:
            node = current_level.popleft()
            current_answer.append(node.val)

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

            if not current_level:
                answer.append(current_answer)
                current_level = deque(next_level)
                next_level = []
                current_answer = []
        
        return answer