class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True

        def helper(string):
            return True if string == string[::-1] else False
        
        if helper(s):
            return True
        
        for i in range(len(s)):
            if helper(s[0:i]+s[i+1:]):
                return True
        
        return False


class Solution:
    def validPalindrome(self, s):
        def helper(i, j):
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return helper(i + 1, j) or helper(i, j - 1)
        return True