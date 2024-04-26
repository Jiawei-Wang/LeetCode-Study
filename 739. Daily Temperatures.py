# 1. 理解题意：找到每个元素和它后面第一个大于它的元素之间的距离
# 2. go through example
# 3. clarify assumptions: what format is input, range of input, length of input, corner cases
# 4. 暴力解：time n^2 space 1
# 5. use stack: time n space n
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        ans = [0] * len(temperatures)
        
        # for index, value in enumerate(temperatures[::-1]):
        # 使用上面这个语法时，每个元素的index会被翻过来，举例：temperatures = [a,b,c]
        # 输出的是：0,c    1,b     2,a
        
        index = len(temperatures)-1
        for value in temperatures[::-1]:
            if not stack:
                stack.append((value,index))
            else:
                while stack and stack[-1][0] <= value:
                    stack.pop()
                if stack:
                    ans[index] = stack[-1][1] - index
                else:
                    ans[index] = 0
                stack.append((value,index))
            index -= 1
        return ans


# https://www.youtube.com/watch?v=WGm4Kj3lhRI
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
          while stack and T[stack[-1]] < t:
            cur = stack.pop()
            ans[cur] = i - cur
          stack.append(i)

        return ans


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        stack = []
        for index, element in enumerate(temperatures):
            while stack and stack[-1][1] < element:
                topElement = stack.pop()
                answer[topElement[0]] = index - topElement[0]
            stack.append([index, element])
            answer.append(0)
        return answer


# 2024
from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        answer = [0] * length
        stack = deque()
        for index in range(length):
            value = temperatures[index]
            while stack and stack[-1][0] < value:
                last = stack.pop()
                answer[last[1]] = index - last[1]
            stack.append([value, index])
        return answer