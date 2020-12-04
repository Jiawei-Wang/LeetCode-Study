"""
Three possible cases depending upon the input:
    1) All consecutive pairs of digits are not decreasing (e.g. 123, 122, 111) => input is good already
    2) Otherwise note the first decreasing pair index (decIdx)
    2.1) there is no increasing pair before the decreasing pair (e.g. 210, 220, 212):
         Decrease first digit by 1 and fill rest with 9's.
    2.2) there is an increasing pair before the decreasing pair (e.g. 120, 1230):
         Find the last increasing pair before decIdx -> incIdx
            - decrease the original digit at incIdx by 1 (as it's the second element of an increasing pair it is always > 0)
            - left of incIdx => same as original
            - right of incIdx => fill 9's
"""


class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        # 遍历时遇到的最近一个increasing pair的后一位的index
        inc = 0
        
        N = str(N)
        length = len(N)
        
        for i in range(1, length):
            if int(N[i]) > int(N[i-1]):
                inc = i
            if int(N[i]) < int(N[i-1]):
                # 2.1
                if inc == 0:
                    return int(str(int(N[0])-1)+"9"*(length-1))
                # 2.2
                else:
                    return int(N[:inc]+str(int(N[inc])-1)+"9"*(length-inc-1))
        # 1
        return int(N) 