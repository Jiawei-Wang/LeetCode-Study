class Solution:
    def repeatedCharacter(self, s: str) -> str:
        occur = set()
        for char in s:
            if char in occur:
                return char
            occur.add(char)