# DP
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # s as number of cols (horizontal), t as number of rows (vertical)
        cols = len(s) + 1
        rows = len(t) + 1

        # we have an extra col and an extra row to represent empty string
        # dp[i][j] = k: we have k t[0:i] in s[0:j]
        dp = [[0] * cols for _ in range(rows)] 

        # when t is empty, any s[0: c] has one and only one t in it
        # so first row (horizontal) is all 1s
        for c in range(cols): 
            dp[0][c] = 1

        # when t is non-empty and s is empty, there is no t in it
        # so first col (vertical) is all 0s
        # we already have them as 0 so nothing to do
        
        # starting from first char in s and first char in t (second row, second col)
        for x in range(1, cols): # we are at char s[x-1]
            for y in range(1, rows): # we are at char t[y-1]

                # on current row, we move to the right side
                # which means we are expanding s on the same t

                # for example 
                # "ra" has 1 "ra"
                # "rab" has 1 "ra" (same as "ra")
                # "rabb" has 1 "ra" (same as "rab")
                # so if chars don't match, just get the same value from left
                if s[x - 1] != t[y - 1]: 
                    dp[y][x] = dp[y][x - 1]

                # for example
                # "rabb" has 2 "rab"
                # "rabb" has 1 "rabb"
                # "rabbb" has 3 "rabb"
                # so if chars match, get the value from both left and topleft
                # why: see below
                else:
                    dp[y][x] = dp[y - 1][x - 1] + dp[y][x - 1]

        return dp[-1][-1]

        # hardest part of this question is state transition
        # when s[i-1] != t[j-1]: dp[i][j] = dp[i-1][j]  
        # when s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j] + dp[i-1][j-1] 
        # first one is easy: 
        # there is 3 "ab" in "abab"
        # (first a first b, first a second b, second a second b)
        # there is still 3 "ab" in "ababc" (c doesn't serve any purpose)
        # there is still 3 "ab" in "ababa" (because subsequence must end with b, last a doesn't serve any purpose)
        # second one is hard:
        # there is 3 "ab" in "abab"
        # there is 1 "abb" in "abab"
        # there is 4 "abb" in "ababb"
        # why use 3 + 1 = 4
        # for last b in "ababb", we have two choices: use it or not use it
        # 1. if we don't use last b in "ababb", question is the same as how many "abb" in "abab" 
        # 2. if use last b in "ababb", question is the same as how many "ab" in "abab"
        # another example:
        # there is 1 "a" in "ac" 
        # there is 1 "ac" in "ac"
        # there is 2 "ac" in "acc"
        # if we don't use last c: we get same as finding "ac" in "ac"
        # if we use last c: we get same as finding "a" in "ac"