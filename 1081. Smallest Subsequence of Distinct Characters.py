class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occur = {char: index for index, char in enumerate(s)}
        seen = set()
        stack = []

        for i, c in enumerate(s):
            if c in seen:
                continue
            
            while stack and c < stack[-1] and i < last_occur[stack[-1]]:
                seen.remove(stack.pop())
            
            stack.append(c)
            seen.add(c)

        return "".join(stack)