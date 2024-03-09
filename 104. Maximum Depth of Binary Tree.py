# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursion + DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
"""
对上面答案的理解：
因为是recursion所以需要有base case
每一层和下一层的区别在于+1
因为程序会一直搜索直到找到左子树的高度，再去访问右子树，所以是DFS
"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        """
        num_node_level用于检测本层是否遍历完毕，原理如下：
        1. 假设本层有2个元素，num_node_level=2
        2. 在加入新的元素时，num_node_level-=1
        3. 当num_node_level=0时本层自动结束，worklist中剩余的元素必定是在遍历本层元素时被加入worklist的下一层元素
        4. 一共会被加入最多4个元素，num_node_level会被设定为对应数字
        """
        worklist = collections.deque([root])
        num_node_level = 1
        levels = 0
        while worklist:
            node = worklist.popleft()
            if node.left:
                worklist.append(node.left)
            if node.right:
                worklist.append(node.right)
            num_node_level -= 1
            if num_node_level == 0:
                levels += 1
                num_node_level = len(worklist)
                
        return levels


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def level(node):
            if not node: 
                return 0
            elif node.left and node.right:
                return 1 + max(level(node.left), level(node.right))
            elif node.left:
                return 1 + level(node.left)
            elif node.right:
                return 1 + level(node.right)
            else:
                return 1

        return level(root)
        