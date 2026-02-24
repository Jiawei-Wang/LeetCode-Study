class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        pairs, sym, nonPaired = 0, 0, Counter()
        for w in words:
            if nonPaired[w[:: -1]] > 0: # if we already have a counter word in hashmap
                pairs += 1 # both of them are used to form a pair
                nonPaired[w[:: -1]] -= 1 # counter word is removed
                sym -= 1 if w[0] == w[1] else 0 # counter word is also removed from symmetric 
            else: # if this word has no counter word (yet)
                nonPaired[w] += 1 # add it to the hashmap
                sym += 1 if w[0] == w[1] else 0 # if it's symmetric, add it to symmetric
        return pairs * 4 + (2 if sym > 0 else 0) # we use all paird words and at most 1 symmetric word