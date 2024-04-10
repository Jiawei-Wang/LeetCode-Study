class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False

        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]
            for i in range(first, first + k):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0: # a key can only be exhausted when it's the head of a group
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True