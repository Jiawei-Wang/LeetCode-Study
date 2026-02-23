class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        answer = []
        for word in words:
            array = word.split(separator)
            answer.extend([string for string in array if string])
        return answer