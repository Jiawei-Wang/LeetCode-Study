class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        c = int(a.split("+")[0])
        d = int(a.split("+")[1].replace("i", ""))
        e = int(b.split("+")[0])
        f = int(b.split("+")[1].replace("i", ""))

        return str(c*e-d*f) + "+" + str(c*f+d*e) + "i"
        
