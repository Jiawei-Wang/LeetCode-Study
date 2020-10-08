# 按照java版答案修改
class Solution:
    def compress(self, chars: List[str]) -> int:
        edit = 0
        loop = 0
        while loop < len(chars):
            current_char = chars[loop]
            count = 0

            while loop < len(chars) and chars[loop] == current_char:
                loop += 1
                count += 1
            chars[edit] = current_char
            edit += 1
            if count > 1:
                for char in list(str(count)):
                    chars[edit] = char
                    edit += 1
        return edit
