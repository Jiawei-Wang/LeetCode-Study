from collections import Counter
import re

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def contains_all_chars(source, target):
            return not (Counter(target) - Counter(source))

        license = re.sub(r'[^a-zA-Z]', '', licensePlate).lower()
        
        answer = None
        length = float("inf")
        for word in words:
            if contains_all_chars(word, license):
                if len(word) < length:
                    answer = word
                    length = len(word)
        return answer

        