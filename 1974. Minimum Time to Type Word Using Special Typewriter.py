class Solution:
    def minTimeToType(self, word: str) -> int:
        current = "a"
        count = 0
        for char in word:
            abs_distance = abs(ord(current) - ord(char))
            distance = min(abs_distance, 26 - abs_distance)
            count += distance + 1
            current = char
        return count
