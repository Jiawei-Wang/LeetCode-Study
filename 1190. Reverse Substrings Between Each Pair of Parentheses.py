# brute force
# time O(n^2)
# space O(n)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = [''] # base layer
        
        for c in s:
            if c == '(':
                res.append('') # start a new layer 
            elif c == ')':
                res[len(res) - 2] += res.pop()[::-1] # pop current layer, reverse it, append to previous layer
            else:
                res[-1] += c # append to current layer

        return "".join(res)