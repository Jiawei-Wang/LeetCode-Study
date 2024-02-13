# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # get all paths
        allPath = []
        rootPath = []
        
        def bfs(node, currentPath):
            if node.left:
                bfs(node.left, currentPath + [node.val])
            if node.right:
                bfs(node.right, currentPath + [node.val])
            if not node.left and not node.right:
                allPath.append(currentPath + [node.val])

        bfs(root, rootPath)

        # count palindrome paths
        ans = 0
        for path in allPath:
            checkSet = set()
            for val in path:
                if val in checkSet:
                    checkSet.remove(val)
                else:
                    checkSet.add(val)
            if len(checkSet) == 1 or len(checkSet) == 0:
                ans += 1
        return ans


class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def bfs(node, currentPath):
            # use a set to add new value and remove existing value (duplicate check)
            if node.val in currentPath:
                currentPath.remove(node.val)
            else:
                currentPath.add(node.val)
            
            # go one layer deeper
            if node.left:
                bfs(node.left, currentPath.copy()) # use a copy to preserve current state, otherwise everything will happen in the same set
            if node.right:
                bfs(node.right, currentPath.copy())
            if not node.left and not node.right:
                allPath.append(currentPath) # we arrive at leaf and put the set into collection

        if not root:
            return 0

        allPath = []
        rootPath = set()
        bfs(root, rootPath)

        ans = 0
        for path in allPath:
            if len(path) <= 1: # if there is only one element or no element in the set, the path is palindromic
                ans += 1
        return ans




