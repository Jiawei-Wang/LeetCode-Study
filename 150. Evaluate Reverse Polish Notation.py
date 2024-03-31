class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # It is guaranteed that the given RPN expression is always valid
        if len(tokens) == 1:
            return int(tokens[0])
        stack = deque([tokens[0], tokens[1]])
        i = 2
        while i < len(tokens):
            if tokens[i] in '+-*/':
                a = int(stack.pop())
                b = int(stack.pop())
                if tokens[i] == '+':
                    result = a + b
                elif tokens[i] == '-':
                    result = b - a
                elif tokens[i] == '*':
                    result = a * b
                else:
                    # 除法的原则是向0靠近，比如4/3=1, 4/-3=-1而不是-2
                    result = abs(b)//abs(a)
                    if b*a < 0:
                        result *= -1
                stack.append(result)
            else:
                stack.append(tokens[i])
            i += 1
        return int(stack[0])
                    

# 对上面代码的优化（解法相同）
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l+r)
                elif t == "-":
                    stack.append(l-r)
                elif t == "*":
                    stack.append(l*r)
                else:
                    stack.append(int(float(l)/r)) 
                    # print(-2//3)                   -1
                    # print(int(float(-2)/3))         0
        return stack.pop()
                    

from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def divide(a, b):
            if (a >= 0 and b > 0) or (a < 0 and b < 0):
                return a // b
            else:
                return -(-a//b) if a % b != 0 else a//b

        operations = set(['*', '/', '+', '-'])
        stack = deque()
        for token in tokens:
            if token in operations:
                second = stack.pop()
                first = stack.pop()
                if token == '+':
                    stack.append(first + second)
                elif token == '-':
                    stack.append(first - second)
                elif token == '*':
                    stack.append(first * second)
                else:
                    stack.append(divide(first, second))
            else:
                stack.append(int(token))
        
        return stack.pop()

        