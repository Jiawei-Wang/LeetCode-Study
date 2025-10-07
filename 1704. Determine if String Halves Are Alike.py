class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)//2 # s is of even length
        first = s[:n]
        second = s[n:]

        def count_vow(string):
            hashset = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
            count = 0
            for char in string:
                if char in hashset:
                    count += 1
            return count
        
        return count_vow(first) == count_vow(second)


