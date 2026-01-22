class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        array = s.split(" ")
        return " ".join(array[0:k])
        