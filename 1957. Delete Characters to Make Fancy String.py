class Solution:
    def makeFancyString(self, s: str) -> str:
        output = [s[0]]     
        current = s[0]
        count = 1
        for i in range(1, len(s)):
            if s[i] == current:
                count += 1
                if count >= 3:
                    continue
                else:
                    output.append(s[i])
            else:
                current = s[i]
                count = 1
                output.append(s[i])
        return "".join([char for char in output])
        