# 创建一个stack
# 依次将char加入，如果当前的char可以和stack顶部元素组成一对，则二者被cancel
# 最后stack中剩下的就是没有配对的char，它们之间的index之差即为一个符合要求的substring的长度
# 找到全局最长的那个即可
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 先遍历找出所有没有配对的char
        n = len(s)
        longest = 0
        stack = []
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    if s[stack[-1]] == '(':
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
        
        # 然后将stack中元素取出，找出index之差最大的
        if not stack:
            longest = n
        else:
            a = n
            b = 0
            while stack:
                b = stack.pop()
                longest = max(longest, a-b-1)
                a = b
            longest = max(longest, a)
        return longest


# 优化：在建stack时就去计算index之差