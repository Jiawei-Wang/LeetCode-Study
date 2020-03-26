class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


'''
The isupper() methods returns “True” if all characters in the string are uppercase, Otherwise, It returns “False”
The islower() methods returns “True” if all characters in the string are lowercase, Otherwise, It returns “False”.
The istitle() methods returns “True” if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
'''
