class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:        
        nums.sort()
        dp = [1] * len(nums) # store the length of longest subset that ends at this index
        prev = [-1] * len(nums) # store previous number for current number/index (so we can backtrack to reconstrcut the subset)
        maxi = 0 # store the global longest subset that ends at this index

        for i in range(1, len(nums)): # each new index, we need to check if it can appended to a subset
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1: # found a longer one
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > dp[maxi]: # found a global better one 
                maxi = i
        
        # reconstruct global longest subset
        res = []
        i = maxi
        while i >= 0:
            res.append(nums[i])
            i = prev[i]
        return res




