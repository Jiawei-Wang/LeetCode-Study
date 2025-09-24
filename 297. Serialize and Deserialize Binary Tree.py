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
        # storing node value is easy
        # storing tree shape is hard
        vals = []

        def encode(node): 
            if node:
                vals.append(str(node.val))
                encode(node.left)
                encode(node.right)
            else:
                vals.append('#')
        
        encode(root)
        return ' '.join(vals)
        # we preorder traverse the tree, so the string stores order information
        # leaf nodes are followed by two #
        # so the shape of the tree is fully stored in the string
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split()) # vals是一个iter，next(vals)每次会按顺序返回vals中下一个元素

        def decode():
            # preorder it again
            val = next(vals) 

            if val == '#':
                return None
            
            node = TreeNode(int(val))
            node.left = decode()
            node.right = decode()
            
            return node
        
        return decode()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# both serialize and deserialize need to traverse the tree in same order
# shape of the tree will be stored by using # to mark end of path
class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()