class Solution:
    def minAddToMakeValid(self, S):
        # easiest way to make string valid is to add
        # parentheses to the left and right side of string
        left = 0 # how many "(" we need on the left of S
        right = 0 # how many ")" we need on the right of S

        # so now we just need to find out 
        # how many opened parentheses in S
        for i in S:
            if right == 0 and i == ')':
                left += 1
            else:
                if i == '(':
                    right += 1  
                else:
                    right -= 1
        return left + right