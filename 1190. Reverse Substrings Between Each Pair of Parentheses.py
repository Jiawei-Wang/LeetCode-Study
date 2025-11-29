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


# skip inner parentheses 
# two passes
# time O(n)
# space O(n)
class Solution:
    def reverseParentheses(self, s: str) -> str:
        # ------------------------------------------------------------
        # Step 1: Build a mapping between matching parentheses
        # ------------------------------------------------------------
        stack = []
        pair = {}  # maps each '(' to its matching ')' and vice versa
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                j = stack.pop()
                # Create bi-directional mapping
                pair[i] = j
                pair[j] = i

        # ------------------------------------------------------------
        # Step 2: Traverse the string, jumping across parentheses
        # ------------------------------------------------------------
        result = []
        i = 0       # current index
        direction = 1  # +1 means forward, -1 means backward
        
        while 0 <= i < len(s):
            if s[i] in "()":
                # Jump to matching parenthesis
                i = pair[i]
                # Reverse direction whenever we pass through parentheses
                direction = -direction
            else:
                # Normal characters are collected
                result.append(s[i])
            
            i += direction  # Move in current direction

        return "".join(result)
