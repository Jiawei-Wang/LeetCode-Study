# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 理解错了题意，它问的不是让我遍历右子树，而是问让我返回从树的右侧观察树，能够看到的node的集合
# 举例：
#       1
#    2     3
#   4 5 None None
# 那么能够观察到的就是[1,3,5]
# 一个极端的例子：
#      1
#    2   none
#  3   none
# 返回的是[1,2,3]
# 所以题目要求的是寻找每一行最右边的node


# BFS，和找出数的高度题目一样，每次将当前一轮queue中元素全部pop完毕后，将最后一个被pop的放入答案中
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            level = len(queue)
            while level != 0:
                cur = queue.popleft()
                if cur.left: # 两个if statement顺序不能反，这决定了queue中每行node的顺序
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                level -= 1
                if level == 0:
                    ans.append(cur.val)
        
        return ans


# Recursion: combine left and right
# Compute the right view of both right and left left subtree, then combine them. For very unbalanced trees, this can be O(n^2), though.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        
        return [root.val] + right + left[len(right):]
    
"""
对上面答案的模拟：
     ->                1
     ->           2       3
     ->        4    5   6    x
     ->      7  8 
     ->    9  x
元素9返回：[9]
元素7返回：[7,9]
元素4返回：[4,8,9]
元素2返回：[2,5,8,9]
元素1返回：[1,3,6,8,9]
"""


# Recursive, first come first serve
# DFS-traverse the tree right-to-left, add values to the view whenever we first reach a new record depth. This is O(n).
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def collect(node, depth):
            if node:
                if depth == len(view): # 如果此时是第n层，且正好view中有n个元素，则将该元素加入
                    view.append(node.val)
                collect(node.right, depth+1) # 从右侧开始遍历
                collect(node.left, depth+1)
        view = []
        collect(root, 0)
        return view
    
"""
对答案的理解：从右侧开始DFS这棵树，每次进入新的一层时，已经决定第一个找到的元素是该层最右边的元素，那么直接加入即可
"""


