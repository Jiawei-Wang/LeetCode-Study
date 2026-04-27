class Solution:
    def minimumChairs(self, s: str) -> int:
        counter = 0
        max_counter = 0
        for char in s:
            if char == "E":
                counter += 1
                max_counter = max(max_counter, counter)
            else:
                counter -= 1
        return max_counter
        