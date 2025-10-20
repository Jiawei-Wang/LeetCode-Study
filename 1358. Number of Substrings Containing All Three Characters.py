class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {char: 0 for char in 'abc'}
        res = 0
        left = 0
        for right in range(len(s)): 
            count[s[right]] += 1
            while all(count.values()): # while all values in count are true
                count[s[left]] -= 1
                left += 1
            res += left
        return res