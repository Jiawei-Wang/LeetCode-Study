class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        # dp[lane] = minimum side jumps needed to be in this lane at current position.
        dp = [1, 0, 1] # at the starting position, we are on lane 2 

        # for each position i
        for position in obstacles[1:]:
            if position != 0: # if there is an obstacle
                dp[position - 1] = float('inf') # this lane is not accessable

            for i in range(3):
                if position != i + 1: # if this lane has no obstacle at this position
                    # Staying in lane k: cost dp[k]
                    # Jumping sideways into lane k: cost 1 + min(other lanes)
                    # dp[k] = min(dp[k], 1 + min(dp[other lanes]))
                    dp[i] = min(dp[i], dp[(i + 1) % 3] + 1, dp[(i + 2) % 3] + 1)
                    
        return min(dp)