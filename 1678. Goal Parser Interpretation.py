class Solution:
    def interpret(self, command: str) -> str:
        array = []
        length = len(command)
        i = 0
        while i+1 < length:
            current = command[i]
            if current == "G":
                array.append("G")
                i += 1
            else:
                if command[i+1] == ")":
                    array.append("o")
                    i += 2
                else:
                    array.append("al")
                    i += 4
        
        if i+1 == length:
            array.append("G")
        
        return "".join(array)


class Solution:
    def interpret(self, s: str) -> str:
        d = {"(al)":"al", "()":"o","G":"G"}
        tmp= ""
        res=""
        for i in range(len(s)):
            tmp+=s[i]
            if tmp in d:
                res += d[tmp]
                tmp = ""
        return res
