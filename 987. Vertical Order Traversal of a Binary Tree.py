# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # return 2d array: arrays are sorted by column number (left to right)
        # within each 1d array: elements are sorted by row number (top to down)
        # if elements have same column number within the same row, sort by value
        # so basically this question is asking to sort by column, then by row, then by value

        nodes = [] # (column, row, value)
        
        # 1. Traverse
        queue = deque([(root, 0, 0)]) # (node, row, col)
        while queue:
            node, row, col = queue.popleft()
            if node:
                nodes.append((col, row, node.val))
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))
        
        # 2. Sort the nodes
        # Python's sort will sort by col, then by row, then by value
        nodes.sort()
        
        # 3. Group by column
        result_dict = defaultdict(list)
        for col, row, val in nodes:
            result_dict[col].append(val)
            
        # 4. Return values in sorted column order
        return [result_dict[key] for key in sorted(result_dict.keys())]

