# change unmatched parentheses to empty char
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s) # modify on list not on string
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else: # if a close has no open to match
                    s[i] = ''
        while stack: # all extra open(s)
            s[stack.pop()] = ''
        return ''.join(s)

