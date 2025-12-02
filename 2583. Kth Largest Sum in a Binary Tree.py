class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        current_level = [root]
        max_heap = []
        heapq.heapify(max_heap)

        while current_level:
            level_sum = 0
            next_level = []

            for node in current_level:
                level_sum += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # Maintain a min-heap of size k tracking the k largest sums
            if len(max_heap) < k:
                heapq.heappush(max_heap, level_sum)
            else:
                heapq.heappushpop(max_heap, level_sum)

            current_level = next_level
        
        if len(max_heap) < k:
            return -1
        
        return max_heap[0]  # the k-th largest
