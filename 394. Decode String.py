class Solution:
    def decodeString(self, s: str) -> str:
        """
        When we hit an open bracket, we know we have parsed k for the contents of the bracket, so 
        push (current_string, k) to the stack, so we can pop them on closing bracket to duplicate
        the enclosed string k times.
        """
        stack = []
        current_string = ""
        k = 0

        for char in s:
            if char == "[":
                # Just finished parsing this k, save current string and k for when we pop
                stack.append((current_string, k))
                # Reset current_string and k for this new frame
                current_string = ""
                k = 0
            elif char == "]":
                # We have completed this frame, get the last current_string and k from when the frame 
                # opened, which is the k we need to duplicate the current current_string by
                last_string, last_k = stack.pop(-1)
                current_string = last_string + last_k * current_string
            elif char.isdigit():
                k = k * 10 + int(char)
            else:
                current_string += char

        return current_string
    
    """
    对答案的理解：
    一次遍历，遍历过程中可能遇到的char有4种
    1. 数字（数字后面会跟一个左括号）
    2. 左括号（开始记录string）
    3. 右括号（string记录完毕）
    4. 字母（组成string）
    
    遍历时会遇到的正常情况：数字 + 左括号 + 字符 + 右括号
    同时也可能会遇到括号中嵌套括号的情况
    
    每次遇到左括号，将当前这一层的k，以及它前面的string保存进stack
    每次遇到右括号，将前面一层的string，与（当前这一层的string，与这一层的k相乘）相加
    
    举例： 4[ac]
    那么stack里会放入（''，4)，在遇到右括号后会让current_string = '' + 4 * 'ac'
    
    举例：4[a2[c]]
    那么stack里会放入（''，4)，然后放入('a', 2)，遇到第一个右括号后current_string = 'a' + 2 * 'c'，遇到第二个右括号后current_string = '' + 4 * 'acc'
    """


class Solution:
    def decodeString(self, s: str) -> str:
        current_string = ""
        stack = []
        counter = 0

        for char in s:
            if char.isdigit():
                counter = counter * 10 + int(char)
            elif char == "[":
                stack.append((current_string, counter))
                current_string = ""
                counter = 0
            elif char == "]":
                last_string, last_counter = stack.pop(-1)
                current_string = last_string + last_counter * current_string
            else:
                current_string += char

        return current_string