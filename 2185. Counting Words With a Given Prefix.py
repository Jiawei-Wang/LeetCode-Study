class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        length = len(pref)
        def contains_prefix(word):
            if word[0:length] == pref:
                return True
        count = 0
        for word in words:
            if contains_prefix(word):
                count += 1 
        return count
