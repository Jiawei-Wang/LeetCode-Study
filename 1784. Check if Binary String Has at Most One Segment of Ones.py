class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        has_zero = False
        for char in s:
            if char == "0":
                has_zero = True
            if has_zero and char == "1":
                return False
        return True

        