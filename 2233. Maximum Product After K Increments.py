# increment minimum number each time
# math: when x > y
# x*(y+1) > (x+1)*y
import heapq
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        # 1×10^9+7 is a large prime number
        MOD = int(1e9 + 7)
        
        # Create a min-heap from the list
        heapq.heapify(nums)

        # Increment the smallest element k times
        for _ in range(k):
            smallest = heapq.heappop(nums)
            heapq.heappush(nums, smallest + 1)

        # Calculate the product modulo MOD
        result = 1
        for num in nums:
            result = (result * num) % MOD
        
        return result
