class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # first we need a sorted counter:
        counts = Counter(nums) # O(n)
        sorted_counts = sorted(counts.items()) # O(klogk) for k unique numbers
        
        # then we use dp in the same way as robbing house question
        dp = [0 for _ in range(len(sorted_counts)+1)]
        dp[1] = sorted_counts[0][0] * sorted_counts[0][1]
        for i in range(1, len(sorted_counts)):
            number = sorted_counts[i][0]
            occur = sorted_counts[i][1]
            index = i + 1
            if number - 1 == sorted_counts[i-1][0]: # if curr number - 1 == prev number
                dp[index] = max(dp[index-1], dp[index-2]+number*occur) # decide if we take it or not
            else: # if they are not next to each other
                dp[index] = dp[index-1]+number*occur # just take it since it's always positive int
        
        return dp[-1]

