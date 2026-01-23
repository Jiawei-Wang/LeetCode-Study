class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if not stack or stack[-1][0] != char:
                count = 1
                stack.append((char, count))
            else: # stack and stack[-1][0] == char
                if stack[-1][1] < k-1: # no enough duplicates yet
                    count = stack[-1][1] + 1
                    stack.append((char, count))
                else:
                    for i in range(k-1):
                        stack.pop()
                    
        return "".join([x for x, y in stack])
