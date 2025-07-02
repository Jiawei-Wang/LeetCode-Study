# time n space 1
class Solution:
    def maxTurbulenceSize(self, A):
        N = len(A)
        anchor = 0 # starting index of current chain
        ans = 1

        def cmp(a, b):
            return (a > b) - (a < b)
            # a > b: 1
            # a = b: 0
            # a < b: -1

        for i in range(1, N): # start from second element, check every comparasion
            c = cmp(A[i-1], A[i])

            # case 1: 0 means old chain ends
            # since we calculated old chain already
            # there is nothing to calculate
            # just start a new chain
            if c == 0:
                anchor = i
            
            # case 2: 1 or -1 and the chain grows
            # do nothing 

            # case 3: 1 or -1 but the chain ends
            # either we arrive at the end of array or two same comparasions 
            elif (i == N-1) or (c * cmp(A[i], A[i+1]) != -1):
                ans = max(ans, i - anchor + 1) # update answer with current chain
                anchor = i # start new chain
        
        return ans
            
