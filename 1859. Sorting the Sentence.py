class Solution:
    def sortSentence(self, s: str) -> str:
        array = s.split(" ")
        answer = ["" for _ in range(9)]
        for candidate in array:
            word = candidate[:len(candidate)-1]
            index = int(candidate[-1])-1
            answer[index] = word
        return " ".join([w for w in answer if w != ""])
