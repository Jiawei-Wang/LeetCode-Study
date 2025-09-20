class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res


class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string)) + "#" + string
        return output

    def decode(self, output: str) -> List[str]:
        answer = []
        i = 0
        current_length = 0
        while i < len(output):
            if output[i] != "#":
                current_length = current_length * 10 + int(output[i])
                i += 1
            else:
                i += 1
                answer.append(output[i:i+current_length])
                i += current_length
                current_length = 0
        return answer
            

