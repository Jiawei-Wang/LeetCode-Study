class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        length = len(s)

        def check(string):
            res = []
            count = dict()
            for index in range(length):
                char = string[index]
                if char in count:
                    count[char].append(index)
                else:
                    count[char] = [index]
            for key, value in count.items():
                res.append(value)
            return res
        
        return check(s) == check(t)


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1, m2 = [0] * 256, [0] * 256 # ASCII size is 256
        n = len(s)
        for i in range(n):
            if m1[ord(s[i])] != m2[ord(t[i])]: # if two chars at same position in s and t have different value 
                return False
            m1[ord(s[i])] = i + 1 # assign two chars at same position in s and t a value (counter in this case)
            m2[ord(t[i])] = i + 1 
        return True