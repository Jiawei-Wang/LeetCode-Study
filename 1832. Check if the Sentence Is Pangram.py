class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        left = set()
        for i in range(26):
            current = chr(ord("a")+i)
            left.add(current)
        
        for char in sentence:
            left.discard(char)
            # set.remove(element): if element is not found, raise KeyError
            # set.discard(element): if element is not found, do nothing
        
        return not left


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26