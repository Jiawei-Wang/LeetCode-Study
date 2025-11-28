class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        count = 0
        for char in s:
            if not stack or stack[-1] == char:
                stack.append(char)
            
            if stack[-1] != char:
                stack.pop()
                if not stack:
                    count += 1
        
        return count
        