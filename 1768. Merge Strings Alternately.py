class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = min(len(word1), len(word2))
        answer = ""
        for i in range(length):
            answer += word1[i] + word2[i]
        if len(word1) > len(word2):
            for i in range(length, len(word1)):
                answer += word1[i]
        else:
            for i in range(length, len(word2)):
                answer += word2[i]
        return answer

        