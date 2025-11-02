class Solution:
    def greatestLetter(self, s: str) -> str:
        hashset = set(s)
        biggest = ""
        for char in hashset:
            if char.swapcase() in hashset:
                biggest = max(biggest, char.upper())
        return biggest

