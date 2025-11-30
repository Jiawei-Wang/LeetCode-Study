class Solution:
    def minOperations(self, s: str) -> int:
        # we want the final string to be either "010101..." or "101010..."
        # for "010101...": 
        # index is [0, 1, 2, 3, ...]
        # and this array mod 2 is: [0, 1, 0, 1, ...] 
        start_with_zero = sum(index % 2 == int(char) for index, char in enumerate(s))
        start_with_one = len(s) - start_with_zero
        return min(start_with_zero, start_with_one)