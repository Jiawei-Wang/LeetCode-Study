class Solution:
    def originalDigits(self, s: str) -> str:
        count = [0] * 10
        for c in s:
            match c:
                # unique ones
                case "z": count[0] += 1 # only zero contains z
                case "w": count[2] += 1 # only two contains w
                case "u": count[4] += 1 # only four contains u
                case "x": count[6] += 1 # only six contains x
                case "g": count[8] += 1 # only eight contains g
                # shared ones 
                case "o": count[1] += 1 # shared by zero, one, two, four
                case "h": count[3] += 1 # shared by three and eight
                case "f": count[5] += 1 # shared by four and five
                case "s": count[7] += 1 # shared by six and seven
                case "i": count[9] += 1 # shared by five, six, eight, nine

        count[1] -= count[0] + count[2] + count[4]
        count[3] -= count[8]
        count[5] -= count[4]
        count[7] -= count[6]
        count[9] -= count[5] + count[6] + count[8]

        answer = []
        for i in range(10):
            for j in range(count[i]):
                answer.append(str(i))
        return "".join(answer)
        
        

        
