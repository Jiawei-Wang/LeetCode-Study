# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root):
        vals = []
        self._serialize(root, vals)
        return ','.join(map(str, vals))
    
    def _serialize(self, root, vals):
        if not root:
            return
        vals.append(root.val)
        self._serialize(root.left, vals)
        self._serialize(root.right, vals)

    # Decodes your encoded data to tree.
    def deserialize(self, data):
        if not data:
            return None
        vals = list(map(int, data.split(',')))
        from collections import deque
        q = deque(vals)
        return self._deserialize(q, float('-inf'), float('inf'))
    
    def _deserialize(self, q, lower, upper):
        if not q:
            return None
        if q[0] < lower or q[0] > upper:
            return None
        val = q.popleft()
        root = TreeNode(val)
        root.left = self._deserialize(q, lower, val)
        root.right = self._deserialize(q, val, upper)
        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans