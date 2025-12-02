class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        answer = 0
        for string in strs:
            if string.isdigit():
                answer = max(answer, int(string))
            else:
                answer = max(answer, len(string))
        return answer