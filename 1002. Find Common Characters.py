class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return [char for char in words[0]]

        def count(word):
            array = [0] * 26
            for char in word:
                array[ord(char)-ord("a")] += 1
            return array
        
        def compare(a1, a2):
            array = [0] * 26
            for i in range(26):
                array[i] = min(a1[i], a2[i])
            return array

        target = count(words[0])

        for i in range(1, len(words)):
            curr = count(words[i])
            target = compare(target, curr)
        
        answer = []
        for i in range(26):
            for j in range(target[i]):
                answer.append(chr(ord('a') + i))
        return answer
    

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return [char for char in words[0]]

        res = []
        chars = set(words[0])
        for char in chars:
            frequency = min([word.count(char) for word in words])
            res += [char] * frequency
        return res