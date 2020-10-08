class Solution:
    def titleToNumber(self, s: str) -> int:
        # reduce + lambda: 遍历array，将return的值代入下一次循环
        # ord(): 给出字符的Unicode code point, ord("A")=65
        return reduce(lambda x, y : x * 26 + y, [ord(c) - 64 for c in list(s)])

        # 所以整个句子的意思是：把 string 中每个字符对应的值放入array，然后遍历array将其乘以权重，返回总和
        
