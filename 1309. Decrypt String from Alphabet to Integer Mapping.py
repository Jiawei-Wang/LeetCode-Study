# reverse traversal
class Solution:
    def freqAlphabets(self, s: str) -> str:
        s, res = list(s), ''
        while s:
            c = s.pop()
            if c == '#':
                x = s.pop() + s.pop()
                res += chr(ord('a')+int(x[::-1])-1)
            else:
                res += chr(ord('a')+int(c)-1)
        return res[::-1]



        