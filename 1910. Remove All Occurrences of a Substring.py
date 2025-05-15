class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_len = len(part)

        for char in s:
            stack.append(char)
            if len(stack) >= part_len and stack[-part_len:] == list(part):
                for _ in range(part_len):
                    stack.pop()

        return "".join(stack)
