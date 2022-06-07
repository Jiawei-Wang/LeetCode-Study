class Solution:
    def romanToInt(self, s: str) -> int:
        normal = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}
        
        if len(s) == 1:
            return normal[s[0]]
        
        special = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM': 900}
        
        ans = 0
        # check if last two are together
        if s[-2:] in special:
            ans += special[s[-2:]]
            i = 0
            while i < len(s)-2:
                if s[i:i+2] in special:
                    ans += special[s[i:i+2]]
                    i+= 2
                else:
                    ans += normal[s[i]]
                    i+=1
        else:
            ans += normal[s[-1]]
            i = 0
            while i < len(s)-1:
                if s[i:i+2] in special:
                    ans += special[s[i:i+2]]
                    i+= 2
                else:
                    ans += normal[s[i]]
                    i+=1
        return ans


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                z -= roman[s[i]]
            else:
                z += roman[s[i]]
        return z + roman[s[-1]]
            