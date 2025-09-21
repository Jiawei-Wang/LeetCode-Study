# use list
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]":"[", "}":"{", ")":"("} # smart
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []


# use deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque() # append and pop are quicker in deque than list: 1 < n
        for char in s:
            if char == '(':
                stack.append(')') # smart move
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            elif not stack or stack.pop() != char: # when we need to pop: 1. there must still be at least one element in stack, 2. top element must be our target
                return False
        return not stack # at the end of loop, stack should be empty


# totally different idea
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return True
        if n % 2 != 0:
            return False
            
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        
        if s == '':
            return True
        else:
            return False

"""
上面三个解法都涉及了一些corner case的处理
第一个：处理string中有非法元素的情况
第三个：处理string是奇数长度的情况
"""



from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            if char == ")":
                if not stack or stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            elif char == "]":
                if not stack or stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            elif char == "}":
                if not stack or stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        return not stack


class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []
        for char in s:
            if char in hashmap:
                stack.append(hashmap[char])
            else:
                if not stack or (stack[-1] != char):
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0