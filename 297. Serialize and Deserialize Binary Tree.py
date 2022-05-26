# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def encode(node): 
            # 从root开始，将树中每个元素以中左右的形式遍历，放入vals中
            if node:
                vals.append(str(node.val))
                encode(node.left)
                encode(node.right)
            else:
                vals.append('#')
        vals = []
        encode(root)
        return ' '.join(vals)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def decode():
            # 将vals中的元素逐个取出，以中左右的顺序逐个放入新的树中
            val = next(vals) # vals是一个iter，next(vals)每次会按顺序返回vals中下一个元素
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = decode()
            node.right = decode()
            return node
        vals = iter(data.split())
        return decode()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))