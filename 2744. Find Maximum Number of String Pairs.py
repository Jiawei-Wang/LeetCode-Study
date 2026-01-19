class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        # count = 0
        # for i in range(len(words)-1):
        #     for j in range(i+1, len(words)):
        #         if words[i] == words[j][::-1]:
        #             count += 1
        #             break
        # return count

        seen = set()
        count = 0
        for word in words:
            if word[::-1] in seen:
                count += 1
            else:
                seen.add(word)
        return count
