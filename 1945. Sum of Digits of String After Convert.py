class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def transform(input):
            total = 0
            for num in input:
                for digit in num:
                    total += int(digit)
            return str(total)
        
        arr = []
        for char in s:
            arr.append(str(ord(char)- ord("a")+1))
        
        joined = "".join(arr)
        for i in range(k):
            joined = transform(joined)
        
        return int(joined)
        

