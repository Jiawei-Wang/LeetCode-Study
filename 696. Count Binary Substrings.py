# check every starting point: n^2
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        length = len(s)
        answer = 0
        for i in range(length-1): # valid substring can't start from last char
            counter = 1
            same = True
            for j in range(i+1, length):
                if s[j] == s[i]:
                    if same == False:
                        break
                    counter += 1
                else:
                    counter -= 1
                    same = False
                    if counter == 0:
                        answer += 1
                        break
        return answer


# math: n
class Solution:
    def countBinarySubstrings(self, s):
        # 1. put a space between every 0 and 1
        # 2. split string into list of strings, each only has 0s or 1s
        # 3. get the length of each string, aka length of 0s and 1s groups
        # 4. turn map object into list
        s = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))

        # for example: 00 111 000 11
        # s = [2, 3, 3, 2]
        # two substrings can be formed between 2 and 3, three between 3 and 3, two between 3 and 2
        # return 7
        return sum(min(a, b) for a, b in zip(s, s[1:]))