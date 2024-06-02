class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        deviation = float('inf')
        pq = [] # max heap to store all numbers
        min_n = float('inf') # smallest number in the heap

        # first turn every number into even number and push into heap
        # so we don't have to care about odd number multiply operation anymore
        for n in nums:
            n = n * 2 if n % 2 != 0 else n
            heapq.heappush(pq, -n)
            min_n = min(min_n, n) 

        # for example: nums = [4,1,5,20,3]
        # pq = [-6, -4, -2, -2]
        # min_n = 2

        # now we want to find the minimum deviation among all these numbers in pq = [-6, -4, -2, -2]
        # and we know every number can only be smaller not larger
        # so we do a loop to pick the biggest number each time and divide it by 2
        # and see if we can update current minimum deviation
        # stop when we can no longer change anything in the pq
        while pq and (-pq[0]) % 2 == 0:
            biggest = -heapq.heappop(pq)
            deviation = min(deviation, biggest - min_n)
            min_n = min(min_n, biggest // 2)
            heapq.heappush(pq, -biggest // 2)

        return min(deviation, -pq[0] - min_n)