class Solution:
    def finalString(self, s: str) -> str:
        current = ""
        for char in s:
            if char != "i":
                current += char
            else:
                current = current[::-1]
        return current