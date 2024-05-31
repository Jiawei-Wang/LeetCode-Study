"""
use a stack, cancel out pairs, then after that, the remaining ones will always look like this:
]]]]]]...[[[[[[
we can cancel out at most 2 pairs per swap so swaps needed is:
ceil(m/2). Where m is the number of pairs left

we don't need to actually build the stack
"""
class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        stack_size = 0 # stack only stores "["

        for i in range(len(s)):
            if s[i] == "[":
                stack_size += 1
            elif stack_size == 0:
                count += 1
            else:
                stack_size -= 1
                
        return (count+1)//2