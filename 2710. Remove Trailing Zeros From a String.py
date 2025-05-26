class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        last = len(num)-1
        while last >= 0:
            if num[last] == "0":
                last -= 1
            else:
                return num[:last+1] if last < len(num)-1 else num