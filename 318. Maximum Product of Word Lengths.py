class Solution:
    # brute force
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        for i in words:
            for j in words[words.index(i)+1:]:
                new_i = set(i)
                count = True
                for element in j:
                    if element in new_i:
                        count = False
                if count == True:
                    ans = max(ans, len(i) * len(j))
        return ans


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n

        # Build bitmask for each word
        for i, word in enumerate(words):
            mask = 0
            for ch in set(word):   # set() optional but faster when repeated letters
                mask |= 1 << (ord(ch) - ord('a'))
            masks[i] = mask

        max_prod = 0

        # Compare all pairs
        for i in range(n):
            for j in range(i + 1, n):
                if masks[i] & masks[j] == 0:      # no shared letters
                    prod = len(words[i]) * len(words[j])
                    if prod > max_prod:
                        max_prod = prod

        return max_prod
