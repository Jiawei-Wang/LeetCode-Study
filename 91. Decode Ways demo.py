# DP
"""
Basic idea: solve a problem by solving its subproblem
for example:
    fibonacci sequence: a[0] = 1, a[1] = 1, a[2] = 2, a[3] = 3, a[4] = 5
    so we know a[n] is the sum of a[n-1] and a[n-2]
    so now we just need to get a[n-1] and a[n-2]
    and this problem can be deduced to: do we know a[0] and a[1]?
    the answer is: yes, they are called "base case"
"""
class Solution:
    def numDecodings(self, s: str) -> int: # s = "12031624121118710162410892321016206"
        # corner case
        if not s or s[0]=='0':
            return 0

        # for all other strings, the answer is at least 1
        """
        we create another list dp, and every element in this list represents:
        total num of possible combinations substring [0: i] has
        for example: the value of dp[2] is #combinations for substring "120"
        """
        # using an extra space as first element in the list for buffering
        dp = [0 for x in range(len(s) + 1)] 

        # base case initialization
        # first element is buffer
        # second element represents: s[0] has 1 possible combination(s)
        dp[0:2] = [1,1]

        # from index = 2 (which points to second element in s: s[1])
        for i in range(2, len(s) + 1): 
            # for this element, it has two conditions:
            # 1. as an independent number (same value as dp[i-1])
            # 2. combines with the previous element to form a number (same value as dp[i-2])
            
            # as long as the element is bigger than 0, dp[i] gets the value of dp[i-1]
            if 0 < int(s[i-1:i]):
                dp[i] = dp[i - 1]

            # if the combination falls between 10~26, dp[i] gets the value of dp[i-2]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
                
        return dp[-1]

if __name__ == "__main__":
    test_case = Solution()
    print(test_case.numDecodings("12031624121118710162410892321016206"))