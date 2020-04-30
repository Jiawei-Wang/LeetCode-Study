# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # DFS
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        # 三个原则：
        # 如果当前node和arr中对应元素不相同，或者某一方先走到头，此条路径为false
        # 如果当前node为leaf，检查arr是否到头
        # 其他情况下深度+1然后对两个子树做recursion，如果两个都返回false，则为false
        def dfs(node: TreeNode, depth: int) -> bool:
            if node is None or depth >= len(arr) or arr[depth] != node.val:
                return False
            if node.left == node.right == None:
                return depth + 1 == len(arr)
            return dfs(node.left, depth + 1) or dfs(node.right, depth + 1)
        return dfs(root, 0)

    # BFS
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        # 先判断当前这两个node是否和arr中对应元素相等
        # 如果同时到达leaf和arr尾部返回true
        # 其他情况下，先把当前node的children放入queue，然后再进入下一层
        dq = collections.deque([root])
        for depth, a in enumerate(arr):
            for _ in range(len(dq)):
                node = dq.popleft()
                if node and node.val == a:
                    if depth + 1 == len(arr) and node.left == node.right == None:
                        return True
                    dq.extend(child for child in (node.left, node.right) if child)
        return False
