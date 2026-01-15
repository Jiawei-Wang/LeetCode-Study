# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        visited = dict() # key: value of node, value: TreeNode instance
        not_root = set() # value of nodes that are not root
        for connection in descriptions:
            parent_val = connection[0]
            child_val = connection[1]
            is_left = connection[2]

            if parent_val in visited:
                parent = visited[parent_val]
            else:
                parent = TreeNode(parent_val)

            if child_val in visited:
                child = visited[child_val]
            else:
                child = TreeNode(child_val)
            
            not_root.add(child_val)
            
            if is_left:
                parent.left = child
            else:
                parent.right = child
            visited[parent_val] = parent
            visited[child_val] = child
        
        for key, value in visited.items():
            if key not in not_root:
                return value
        

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        hashmap = {}
        for parent,child,left in descriptions:
            np = hashmap.setdefault(parent, TreeNode(parent)) 
            # understand this line:
            # parent is a variable that contains the data (data is different for each loop)
            # then a TreeNode instance is created using the data (not "parent")
            # if key "parent" exists, return value to np
            # if key "parent" doesn't exist, create value "TreeNode(parent)" in hashmap and return it to np
            # so by running this line, hashmap will have a new key-value pair
            # key: the data, value: the TreeNode instance using this data
            # and np gets the TreeNode instance
            nc = hashmap.setdefault(child, TreeNode(child))
            if left:
                np.left = nc
            else:
                np.right = nc
            children.add(child)
        root = (set(hashmap) - set(children)).pop()
        return hashmap[root]