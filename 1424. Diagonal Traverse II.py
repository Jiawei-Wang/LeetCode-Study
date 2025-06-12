# BFS: treat it like a tree
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        queue = collections.deque([(0, 0)])

        while queue:
            row, col = queue.popleft()
            ans.append(nums[row][col])

            # if an element is on the first col, we add the element below it to the queue
            # (treat the one below as its left child)
            if col == 0 and row + 1 < len(nums):
                queue.append((row + 1, col))

            # then for all elements, we treat the one on the right as its right child
            if col + 1 < len(nums[row]):
                queue.append((row, col + 1)) 
            
        return ans    