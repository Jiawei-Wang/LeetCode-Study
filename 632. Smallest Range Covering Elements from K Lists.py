# nums中每个元素都是一个范围，找到所有范围的共同最小区间（即这个区间中包含每个范围中至少一个元素）
# 举例：
# Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# Output: [20,24]
# Explanation: 
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
class Solution:
    def smallestRange(self, A: List[List[int]]) -> List[int]:
        # Keep a heap of the smallest elements. As we pop element A[i][j], we'll replace it with A[i][j+1]. 
        # For each such element left, we want right, the maximum of the closest value in each row of the array that is >= left, 
        # which is also equal to the current maximum of our heap. We'll keep track of right as we proceed.
        pq = [(row[0], i, 0) for i, row in enumerate(A)]
        heapq.heapify(pq)

        ans = -1e9, 1e9
        right = max(row[0] for row in A)
        while pq:
            left, i, j = heapq.heappop(pq)
            if right - left < ans[1] - ans[0]:
                ans = left, right
            if j + 1 == len(A[i]):
                return ans
            v = A[i][j+1]
            right = max(right, v)
            heapq.heappush(pq, (v, i, j+1))