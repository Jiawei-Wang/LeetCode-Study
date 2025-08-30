# treat it like the robbing house question
# except in robbing house k = 2
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [n for n in nums] # dp[i] = j: best subsequence so far (till i) has sum of j

        for i in range(1, len(nums)):
            for j in range(max(0, i-k), i): # current sum can come from any one of the k previous sums 
                dp[i] = max(dp[i], nums[i] + dp[j])

        return max(dp)


# improve upon the previous answer: 
# when k becomes bigger, comparison is slower since we need to do k comparisons each iteration
# make the comparison part faster with a heap: we can get the biggest sum directly
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # start from nums[0]
        res = nums[0]
        max_heap = [(-nums[0], 0)] # max_sum, index
    
        # then iterate from nums[1]
        for i in range(1, len(nums)):
            # first get rid of the max_sums that are outside of the window 
            while i - max_heap[0][1] > k:
                heapq.heappop(max_heap)
            # now we find a qualified max_sum

            # then we decide if we want to extend the best subsequence we have or start a new one
            cur_max = max(nums[i], nums[i] - max_heap[0][0])
            heapq.heappush(max_heap, (-cur_max, i))

            # last update global answer
            res = max(res, cur_max)
        return res