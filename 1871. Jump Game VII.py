# dp + sliding window
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        dp = [c == '0' for c in s] # dp[i] = True: we can reach i from 0

        # To determine the state of dp[i]
        # we need to check the states in window dp[i-maxJump : i-minJump]
        # and see if there is at least one True in this window
        # but we don't need to recalculate the whole window every time
        # just remove the leftmost dp[i-maxJump-1] and add the rightmost dp[i-minJump]
        
        pre = 0 # number of previous positions that we can jump from

        for i in range(1, len(s)): # i = 0 is always reachable so we don't care about it

            if i - minJump >= 0: 
                pre += dp[i - minJump]
            
            if i - maxJump > 0: 
                pre -= dp[i - maxJump - 1]

            # every step needs to update dp[i] based on pre
            dp[i] &= pre > 0 # same as: dp[i] = dp[i] and (pre > 0)

        return dp[-1]