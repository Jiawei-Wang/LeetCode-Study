# Return the smallest lexicographical string that contains each letter once
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}  # keep track of the last position of each char
        seen = set() # make sure each char appears only once

        stack = []

        for i, c in enumerate(s):
            if c in seen:
                continue
                
            # If a character c is smaller than the top of the stack 
            # and that top character will appear again later
            # we pop it to get a smaller lexicographic order
            while stack and c < stack[-1] and i < last[stack[-1]]:
                seen.remove(stack.pop())
                
            stack.append(c)
            seen.add(c)

        return ''.join(stack)
