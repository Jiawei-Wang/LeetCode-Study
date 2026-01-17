class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            if stack:
                if char == "B" and stack[-1] == "A":
                    stack.pop()
                elif char == "D" and stack[-1] == "C":
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        
        return len(stack)