# n^2
import re

class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            if not s:
                return True

            # Find all starting indexes
            matches = [m.start() for m in re.finditer("abc", s)]

            if matches:
                # Remove substrings by skipping over the matching ranges
                i = 0
                result = []
                match_set = set(matches)

                while i < len(s):
                    if i in match_set:
                        i += 3  # Skip over "abc"
                    else:
                        result.append(s[i])
                        i += 1
                s = ''.join(result)
            else:
                return False
            
    
# stack: n
class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        for i in S:
            if i == 'c':
                if stack[-2:] != ['a', 'b']:
                    return False
                stack.pop()
                stack.pop()
            else:
                stack.append(i)
        return not stack