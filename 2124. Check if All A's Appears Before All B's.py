class Solution:
    def checkString(self, s: str) -> bool:
        flag = False
        for char in s:
            if char == "b" and flag == False:
                flag = True
            if char == "a" and flag == True:
                return False
        return True