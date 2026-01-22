class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}

        def is_valid(word):
            return word[0] in vowels and word[-1] in vowels
        
        count = 0 
        for i in range(left, right+1):
            if is_valid(words[i]):
                count += 1
        return count