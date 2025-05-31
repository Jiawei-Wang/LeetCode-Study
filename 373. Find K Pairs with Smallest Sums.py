# brute force
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        candidates = []
        for first in nums1:
            for second in nums2:
                candidates.append([first,second])
        
        candidates.sort(key=lambda pair: pair[0]+pair[1])

        return candidates[0:k]


# heap
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []
        result = []

        # Only push the first element in nums2 for each element in nums1
        for i in range(min(k, len(nums1))):  # only need the first k rows
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0)) # i, 0: indexes

        # build return array
        while min_heap and len(result) < k:
            # first get the current smallest one
            total, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            # then push new candidate into heap
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result
