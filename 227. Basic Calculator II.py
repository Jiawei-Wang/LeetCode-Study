# 理解题意：求一个没有括号的中缀表达式的结果
# 因为没有括号，所以：
# 1. char不是数字就是操作符
# 2. 遇到乘号或者除号就可以将后面的数字和前面的直接进行操作，不需要等待（最多只会有两个数字进入乘法或者除法运算）
class Solution:
    def calculate(self, s: str) -> int:
        # corner case
        if not s:
            return "0"
        
        # stack的逻辑为：放进去的所有数字都只用加法
        # 遇到减号就*-1然后放进去
        # 遇到乘号和除号就先把两个数合并，再放进去
        stack = []
        
        # 记录当前数字和操作符
        num = 0
        sign = '+'
        
        for i in range(len(s)):
            # 如果遇到数字，则加入当前的num中
            if s[i].isdigit():
                num = num*10+ord(s[i])-ord("0")
                
            # 如果遇到操作符：将当前num进行append操作（此num来自于上一个循环）
            # 如果走到头了（最后一位肯定是数字）：直接进行运算（num来自于此循环刚计算出来的新num，sign来自于最近一次发现的sign）
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                sign = s[i] # sign会出现两种情况：1. 每次遇到操作符则记录下来，2. 最后一轮循环被设为最后一位数字（因为不会再用于计算所以无所谓）
                num = 0
        return sum(stack)