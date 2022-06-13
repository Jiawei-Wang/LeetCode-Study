# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        reverse = False
        while queue:
            cur = [] # 把这层元素装起来
            reverse = not reverse # 每层顺序和上层相反
            level = len(queue) # 此层一共有level个node要处理
            
            while level:
                node = queue.popleft()
                cur.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level -= 1
            if reverse:
                cur.reverse()
            ans.append(reversed(cur))
        return ans