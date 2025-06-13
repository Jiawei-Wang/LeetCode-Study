class Solution:
    def secondHighest(self, s: str) -> int:
        first = second = -1
        for char in s:
            if char.isdigit():
                digit = ord(char) - ord('0')
                if digit > first:
                    first, second = digit, first
                elif first > digit > second:
                    second = digit
        return second
        