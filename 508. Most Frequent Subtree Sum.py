# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        arr = []

        def find_sum(node):
            if not node:
                return 0
            left = find_sum(node.left) if node.left else 0
            right = find_sum(node.right) if node.right else 0
            total = node.val + left + right
            arr.append(total)
            return total 
        find_sum(root)

        def most_frequent_elements(arr):
            freq = defaultdict(int)
            max_count = 0
            result = []
            for num in arr:
                freq[num] += 1
                if freq[num] > max_count:
                    max_count = freq[num]
                    result = [num]  
                elif freq[num] == max_count:
                    if num not in result:
                        result.append(num)  
            return result

        return most_frequent_elements(arr)

            
