class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            counter = 0
            for c in s:
                if c == '(':
                    counter += 1
                elif c == ')':
                    counter -= 1
                    if counter < 0:
                        return False
            return counter == 0

        level = {s}
        while True:
            valid = list(filter(is_valid, level)) # filter applies is_valid to every element in level
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}