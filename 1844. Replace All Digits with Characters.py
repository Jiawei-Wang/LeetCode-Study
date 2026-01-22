class Solution:
    def replaceDigits(self, s: str) -> str:
        array = [char for char in s]
        for i in range(1, len(array), 2):
            char = array[i-1]
            new_char = chr(ord(char)+int(array[i]))
            array[i] = new_char
        return "".join(array)