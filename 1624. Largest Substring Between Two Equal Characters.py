class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hashmap = dict()
        for index in range(len(s)):
            char = s[index]
            if char not in hashmap:
                hashmap[char] = [index]
            else:
                hashmap[char].append(index)

        answer = -1
        for key, value in hashmap.items():
            if len(value) >= 2:
                answer = max(answer, value[-1]-value[0]-1)
        return answer