class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        first = -1
        for i in range(len(word)):
            if word[i] == ch:
                first = i
                break
        if first == -1 or first == 0:
            return word
        else:
            return word[0:first+1][::-1] + word[first+1:]