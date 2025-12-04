class Solution:
    def maximum69Number (self, num: int) -> int:
        string = str(num)
        index = 0
        mark = -1
        while index < len(string):
            if string[index] == "6":
                mark = index
                break
            index += 1
        if mark != -1:
            return int(string[0:index]+"9"+string[index+1:])
        else:
            return num