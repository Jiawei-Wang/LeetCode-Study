class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq = [0 for _ in range(26)]
        for i in range(len(word1)):
            freq[ord(word1[i]) - ord("a")] += 1
            freq[ord(word2[i]) - ord("a")] -= 1
        for f in freq:
            if not -3 <= f <= 3:
                return False
        return True