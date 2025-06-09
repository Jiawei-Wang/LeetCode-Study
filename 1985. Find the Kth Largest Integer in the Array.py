import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        min_heap = []

        for num in nums:
            n = int(num)
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
            else:
                heapq.heappushpop(min_heap, n)

        return str(min_heap[0])
