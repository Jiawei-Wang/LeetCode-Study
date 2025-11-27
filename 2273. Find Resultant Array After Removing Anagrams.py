class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        answer = [words[0]]
        current = Counter(words[0])
        for word in words[1:]:
            if current == Counter(word):
                continue
            else:
                answer.append(word)
                current = Counter(word)
        return answer