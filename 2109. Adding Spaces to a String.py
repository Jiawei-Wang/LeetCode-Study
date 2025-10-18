class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        array = [char for char in s]
        for space in spaces[::-1]:
            array.insert(space, " ")
        return "".join(array)


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        m, n = len(spaces), len(s)
        answer = [' '] * (m+n)
        j = 0
        for i, c in enumerate(s):
            if j < m and i == spaces[j]:
                j += 1
            answer[i+j] = s[i]
        return "".join(answer)       