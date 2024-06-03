class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        length = len(words)
        counter = dict()
        for word in words:
            for char in word:
                counter[char] = counter.get(char, 0) + 1
        for key, value in counter.items():
            if value % length:
                return False
        return True
        