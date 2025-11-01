class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        hashmap = dict()
        for word in words1:
            if word not in hashmap:
                hashmap[word] = 0
            hashmap[word] += 1
        common = set()
        duplicate = set()
        for word in words2:
            if word in hashmap and hashmap[word] == 1:
                if word not in common:
                    common.add(word)
                else:
                    duplicate.add(word)
        return len(common) - len(duplicate)
