# solution1: liberary
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()


# solution2
class Solution:
    def toLowerCase(self, str: str) -> str:
        # string to char list
        char_list = [char for char in str]
        for i in range(len(char_list)):
            if 'A' <= char_list[i] and char_list[i] <= 'Z':
                # 注意 char 和 int 的互相转换方法
                char_list[i] = chr(ord(char_list[i]) - ord('A') + ord('a'))
        # 注意 char list to string 的转换方法
        return ''.join(char_list)
        
