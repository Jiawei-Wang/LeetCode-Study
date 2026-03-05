"""
return value = sum(all picked numbers from nums1) * min(all picked numbers from nums2)
so this is a picking k (nums1[i], nums2[i]) pairs from n available pairs question
which can be solved by using decision tree
however it can't be optimized with DP, since we need to keep track of all picked pairs
the sum and min alone are not enough 
so no dp, and decision tree is too slow

the problem with picking a nums1[i], nums2[i] pair or not is:
change on one side of the formula doesn't guarantee an overall better result
since the other side may make it worse
so we need to eliminate the uncertainty first

imagine if a number M must be chosen to be the minimum from nums2
then all other picks from nums2 must be >= M
in that case, the right side of the formula is fixed 
the only way to maximize return value is to pick largest numbers in nums1 to maximize sum

as mentioned above, a bigger minimum doesn't guarantee a bigger return value, so we still need to compare results
but one thing a bigger minimum can do is that we don't need to worry about updating the minimum every iteration
so a greedy way is to sort nums2 in descending way, so each iteration, we pick the biggest available number
and check if this nums1[i], nums2[i] pair should be picked

check part:
1. if we don't have k pairs yet: pick current pair
2. if we have first k pairs: calculate return value and use it as benchmark
3. for every new pair:
    they are guaranteed to decrease the min(nums2) part
    so we check to see if emitting the smallest element in sum(nums1) part
    and replacing it with the new picked nums1[i] can give us better result
4. iterate till the end of the loop
"""

# use heap to quickly pop and push numbers for sum(nums1) part
import heapq
class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        # 1. Pair them up and sort by nums2 descending
        # This allows us to treat the current nums2 as the 'minimum'
        pairs = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
        
        min_heap = []
        current_sum = 0 # sum(nums1)
        max_total_score = 0
        
        for n1, n2 in pairs:
            # Add current nums1 value to our potential sum
            heapq.heappush(min_heap, n1)
            current_sum += n1
            
            # If we have more than k elements, remove the smallest nums1 value
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)
            
            # If we have exactly k elements, calculate the score
            if len(min_heap) == k:
                # n2 is the minimum because we sorted pairs by nums2 descending
                max_total_score = max(max_total_score, current_sum * n2)
                
        return max_total_score