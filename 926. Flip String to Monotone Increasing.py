# DP
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # subproblem: 
        # for a string s, there are one_count 1s in it and 
        # flip_count flips are required to make it MonoIncr

        # transition:
        # if we add a new char ch to s, we need to update flip_count
        # 1. if ch is "1", then no flip needed
        # 2. if ch is "0":
        #   1) we can flip this "0" to "1" 
        #   2) or we can flip all "1"s in s to "0"
        # so new flip_count = min(flip_count + 1, one_count)
        
        # base case
        one_count = 0
        flip_count = 0

        # iteration
        for ch in s:
            if ch == "1":
                one_count += 1
            else:
                flip_count += 1

            flip_count = min(flip_count, one_count)
        
        return flip_count