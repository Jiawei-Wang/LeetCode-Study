class Solution:
    def checkValidString(self, s: str) -> bool:
        # 读题第一想法：先判断正常的string，把收集到的 * 放在最后评判
        # 但是这样有一个难点：* 的位置对遍历结束的判断有影响，例：**((* 是False，*(*(* 是True

        # 改进：只关心右括号的情况，如果数量过多直接False，如果在末尾数量正好等于需求量，True
        # cmin 是强制要求配对的右括号最小数量
        # cmax 是要求配对的右括号最大数量
        # 例：'(*(', cmin = 1，cmax = 3
        # 如果想要Ture，cmax任何时刻不可以小于0, cmin在结尾必须等于0
        cmin = cmax = 0
        for i in s:
            if i == '(':
                cmax += 1
                cmin += 1
            if i == ')':
                cmax -= 1
                # cmin不小于0
                cmin = max(cmin - 1, 0)
            if i == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0


# 2024
class Solution:
    def checkValidString(self, s: str) -> bool:
        # Use two stacks to keep track of possible open parentheses and asterisks
        open_stack = []
        star_stack = []

        # Iterate through each character in the string
        for i, char in enumerate(s):
            if char == "(":
                open_stack.append(i)  # Store the index of the open parenthesis
            elif char == "*":
                star_stack.append(i)  # Store the index of the asterisk
            else:  # Closing parenthesis encountered
                if open_stack:  # If there are open parentheses
                    open_stack.pop()  # Match with the last open parenthesis
                elif star_stack:  # If there are asterisks
                    star_stack.pop()  # Use the asterisk to match the closing parenthesis
                else:
                    return False  # No open parentheses or asterisks to match with

        # Now, consider remaining asterisks in the stack
        while open_stack and star_stack:
            if open_stack[-1] < star_stack[-1]:  # If an asterisk comes after an open parenthesis
                open_stack.pop()  # Match them
                star_stack.pop()
            else:
                break  # No more valid matches

        return not open_stack  # If all open parentheses are matched, return True



