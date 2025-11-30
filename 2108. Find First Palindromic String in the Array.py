class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindromic(word):
            if word == word[::-1]:
                return True
            return False
        
        for word in words:
            if is_palindromic(word):
                return word
        return ""