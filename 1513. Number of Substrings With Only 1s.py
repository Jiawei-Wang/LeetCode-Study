class Solution:
    def numSub(self, s: str) -> int:
        hashmap = defaultdict(int)

        length = 0
        for i in range(len(s)):
            if s[i] == "0":
                if length != 0:
                    hashmap[length] += 1
                    length = 0
            elif s[i] == "1":
                length += 1
                if i == len(s) - 1:
                    hashmap[length] += 1

        answer = 0
        for key, value in hashmap.items():
            answer += key * (key+1) // 2 * value
        return answer % (10**9 + 7)


class Solution:
    def numSub(self, s: str) -> int:
        mod = 10**9 + 7
        answer = 0
        length = 0

        for char in s:
            if char == "1":
                length += 1
                answer = (answer + length) % mod
                # explain: 
                # Every time you see a 1, the number of new substrings 
                # ending at this 1 is exactly the current length of consecutive 1s
                # for example going from "1111" to "11111"
                # before: 4 * 5 / 2 = 10
                # after: 5 * 6 / 2 = 15
                # extra = 5 = length
            else:
                length = 0

        return answer
