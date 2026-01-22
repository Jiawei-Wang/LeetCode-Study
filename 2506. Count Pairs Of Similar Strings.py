class Solution:
    def similarPairs(self, words: List[str]) -> int:
        wordMap = defaultdict(int)
        for word in words:
            key = ''.join(sorted(set(word)))
            wordMap[key] += 1

        pairs = 0
        for word in wordMap:
            count = wordMap[word]
            pairs += count * (count-1) // 2
        
        return pairs
