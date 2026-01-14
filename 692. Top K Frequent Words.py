import collections
import heapq

class Solution:
    # Time Complexity = O(n + nlogk)
    # Space Complexity = O(n)
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = []
        for key, value in count.items():
            heapq.heappush(heap, Word(value, key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res[::-1]

class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq
    
    def __eq__(self, other):
        return self.freq == other.freq and self.word == other.word


# 2026
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = [set() for _ in range(len(words)+1)]
        # freq[3] = {"I", "love"}
        # I and love both appeared 3 times
        lookup = defaultdict(int) # key: word, value: number of occurrences

        for word in words:
            if lookup[word] != 0:
                freq[lookup[word]].remove(word)
            lookup[word] += 1
            freq[lookup[word]].add(word)
        # for example words = ["i","love","leetcode","i","love","coding"]
        # freq = [set(), {'leetcode', 'coding'}, {'love', 'i'}, set(), set(), set(), set()]
    
        answer = []
        index = len(freq) - 1
        while k != 0 and index >= 0:
            current = freq[index]
            candidates = sorted([word for word in current])
            picked = candidates[:min(k, len(candidates))] # if we have 3 more to pick but have 4 candidates, we can only pick 3
            answer.extend(picked)
            k -= len(picked)
            index -= 1
        return answer



        