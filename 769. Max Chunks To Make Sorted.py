# greedy
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        max_so_far = 0

        for i, val in enumerate(arr):
            max_so_far = max(max_so_far, val)

            # If the max so far equals the index, we can form a chunk
            if max_so_far == i:
                chunks += 1

        return chunks
